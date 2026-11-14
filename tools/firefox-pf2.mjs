// Task 3 PF-2: run the GUI checklist probes in real Firefox (WebDriver BiDi, no extra driver),
// save overlay screenshots to task3-cross-browser/screenshots/PF-2 and results to pf2-results.json.
// Needs backend (fresh: restart it) + Web Admin running and `node tools/seed-orders.mjs` done.
// Usage: node tools/firefox-pf2.mjs ["C:/path/to/firefox.exe"]
import { spawn } from "node:child_process";
import { mkdtempSync, writeFileSync, mkdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const FF = process.argv.slice(2).find((a) => !a.startsWith("--")) || "C:/Users/NHAT DAT/AppData/Local/Mozilla Firefox/firefox.exe";
const OUT = join(ROOT, "task3-cross-browser", "screenshots", "PF-2");
const APP = "http://localhost:5174/";
mkdirSync(OUT, { recursive: true });

// --- launch Firefox with a throwaway profile ---
const profile = mkdtempSync(join(tmpdir(), "hw03-ff-"));
writeFileSync(join(profile, "user.js"), [
  'user_pref("browser.shell.checkDefaultBrowser", false);',
  'user_pref("browser.startup.homepage_override.mstone", "ignore");',
  'user_pref("datareporting.policy.dataSubmissionEnabled", false);',
  'user_pref("browser.aboutwelcome.enabled", false);',
  'user_pref("signon.rememberSignons", false);',
].join("\n"));
process.on("uncaughtException", (e) => { console.error(e); try { ff.kill(); } catch {} process.exit(1); });
const ff = spawn(FF, ["--remote-debugging-port=9333", "-no-remote", "-profile", profile, "-width", "1536", "-height", "860"], { stdio: "ignore" });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let ws;
for (let i = 0; i < 60 && !ws; i++) {
  await sleep(500);
  try {
    ws = await new Promise((ok, bad) => { const s = new WebSocket("ws://127.0.0.1:9333/session"); s.onopen = () => ok(s); s.onerror = bad; });
  } catch {}
}
if (!ws) throw new Error("could not connect to Firefox BiDi");
let seq = 0;
const pending = new Map();
ws.onmessage = (e) => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } };
const cmd = (method, params = {}) => new Promise((ok, bad) => {
  const id = ++seq;
  const timer = setTimeout(() => bad(new Error(`${method}: timeout`)), 45000);
  pending.set(id, (m) => { clearTimeout(timer); m.type === "error" ? bad(new Error(`${method}: ${m.error} ${m.message}`)) : ok(m.result); });
  if (process.env.DEBUG) console.log(">", method);
  ws.send(JSON.stringify({ id, method, params }));
});

const session = await cmd("session.new", { capabilities: { alwaysMatch: { unhandledPromptBehavior: { default: "dismiss" } } } });
const ctx = (await cmd("browsingContext.create", { type: "tab" })).context;
await cmd("browsingContext.setViewport", { context: ctx, viewport: { width: 1536, height: 730 } }).catch(() => {}); // window size already set by -width/-height

const nav = async (url) => { await cmd("browsingContext.navigate", { context: ctx, url, wait: "complete" }); await sleep(1500); };
// evaluate an async function body in the page; returns JSON-decoded value
const run = async (body) => {
  const r = await cmd("script.evaluate", { expression: `(async()=>JSON.stringify(await (async()=>{${body}})()))()`, target: { context: ctx }, awaitPromise: true });
  if (r.type === "exception") throw new Error(r.exceptionDetails.text);
  return JSON.parse(r.result.value ?? "null");
};
const shot = async (name) => { const r = await cmd("browsingContext.captureScreenshot", { context: ctx, origin: "viewport" }); writeFileSync(join(OUT, name), Buffer.from(r.data, "base64")); };
const keys = async (...ks) => cmd("input.performActions", { context: ctx, actions: [{ type: "key", id: "kb", actions: ks.flatMap((k) => [{ type: "keyDown", value: k }, { type: "keyUp", value: k }]) }] });
const hover = async (x, y) => cmd("input.performActions", { context: ctx, actions: [{ type: "pointer", id: "mouse", actions: [{ type: "pointerMove", x: Math.round(x), y: Math.round(y) }] }] });
const TAB = "\uE004", ENTER = "\uE007";

// page helpers injected into every evaluation
const H = `
window.__dlg=window.__dlg||[]; if(!window.__hooked){window.__hooked=1; window.alert=m=>__dlg.push('alert: '+m); window.confirm=m=>{__dlg.push('confirm: '+m);return false};}
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const sv=(el,v)=>{const p=el.tagName==='TEXTAREA'?HTMLTextAreaElement.prototype:el.tagName==='SELECT'?HTMLSelectElement.prototype:HTMLInputElement.prototype;Object.getOwnPropertyDescriptor(p,'value').set.call(el,v);el.dispatchEvent(new Event(el.tagName==='SELECT'?'change':'input',{bubbles:true}))};
const go=async n=>{[...document.querySelectorAll('li')].find(l=>l.textContent.trim()===n).click();await sleep(500)};
const B=t=>[...document.querySelectorAll('button')].find(b=>b.textContent.trim()===t);
const api=async p=>(await (await fetch('http://localhost:3000/api'+p,{headers:{Authorization:'Bearer '+localStorage.adminToken}})).json());
const top0=()=>{window.scrollTo(0,0);const m=document.querySelector('.flex-1');if(m)m.scrollTop=0};
`;
const R = {};

// Mode "down": run while the backend is STOPPED — shows what the UI does with no data (GUI-57/58).
if (process.argv.includes("--backend-down")) {
  await nav(APP);
  await run(`localStorage.adminToken='offline-check';return 1`);
  await nav(APP);
  R.backendDown = await run(H + `await go('Danh mục');return {text:document.querySelector('.flex-1').innerText.slice(0,120),spinner:!!document.querySelector('[class*=animate-]')}`);
  await shot("PF-2_16_backend_down.png");
  writeFileSync(join(ROOT, "task3-cross-browser", "pf2-results-backend-down.json"), JSON.stringify(R, null, 2));
  console.log(JSON.stringify(R));
  ff.kill(); await sleep(1000); try { rmSync(profile, { recursive: true, force: true }); } catch {}
  process.exit(0);
}

// ---------- login screen ----------
await nav(APP);
R.login = await run(H + `return {overlay:document.getElementById('hw03-overlay')?.textContent, h1:document.querySelectorAll('h1').length, h2:[...document.querySelectorAll('h2')].map(h=>h.textContent), inputs:[...document.querySelectorAll('input')].map(i=>i.type), labels:document.querySelectorAll('label').length}`);
await shot("PF-2_01_login.png");
R.loginTests = await run(H + `const ins=()=>document.querySelectorAll('input'), btn=()=>document.querySelector('button'); const o={};
sv(ins()[0],'abc');sv(ins()[1],'x');o.abcValid=ins()[0].checkValidity();btn().click();await sleep(900);o.abc=[...__dlg];__dlg.length=0;
sv(ins()[0],'admin@eshop.com');sv(ins()[1],'wrongpass');btn().click();await sleep(900);o.wrong=[...__dlg];__dlg.length=0;
sv(ins()[0],'test@eshop.com');sv(ins()[1],'Test1234!');btn().click();await sleep(900);o.nonAdmin=[...__dlg];o.stayLogin=!!document.querySelector('input[type=password]');__dlg.length=0;
sv(ins()[0],'admin@eshop.com');sv(ins()[1],'Admin123!');btn().click();await sleep(1500);o.loggedIn=[...document.querySelectorAll('h2')].map(h=>h.textContent);return o`);

// ---------- DOM audit + main screens ----------
R.audit = await run(H + `const lum=c=>{const [r,g,b]=c.match(/\\d+/g).slice(0,3).map(v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4});return 0.2126*r+0.7152*g+0.0722*b};
const ratio=(a,b)=>{const [x,y]=[lum(a),lum(b)].sort((p,q)=>q-p);return +((x+0.05)/(y+0.05)).toFixed(2)};
const bgOf=el=>{while(el){const c=getComputedStyle(el).backgroundColor;if(c!=='rgba(0, 0, 0, 0)'&&c!=='transparent')return c;el=el.parentElement}return 'rgb(255,255,255)'};
const out={},low={};
for(const n of ['Dashboard','Danh mục','Sản phẩm','Mã Giảm Giá','Đơn hàng','Người dùng']){await go(n);const m=document.querySelector('.flex-1');const li=[...document.querySelectorAll('li')].find(l=>l.textContent.trim()===n);
out[n]={h1:[...document.querySelectorAll('h1')].map(h=>h.textContent).join(),labels:m.querySelectorAll('label').length,inputs:[...m.querySelectorAll('input,select')].map(i=>i.type+(i.required?'*':'')+(i.min?':min'+i.min:'')+(i.accept?':'+i.accept:'')).join(' '),
btn:[...new Set([...m.querySelectorAll('button')].map(b=>b.textContent.trim()+'='+getComputedStyle(b).backgroundColor))].join(' | '),active:getComputedStyle(li).color,liTab:li.tabIndex,scroll:[m.scrollWidth,m.clientWidth],cells:[...m.querySelectorAll('td')].slice(0,5).map(t=>t.textContent.trim()).join(' / ')};
for(const el of m.querySelectorAll('button,h3,p,td span')){const t=el.textContent.trim().slice(0,18);if(!t||t in low)continue;const r=ratio(getComputedStyle(el).color,bgOf(el));if(r<4.5)low[t]=r}}
await go('Dashboard');return {out,low}`);
const screens = [["Dashboard", "02_dashboard"], ["Danh mục", "03_categories"], ["Sản phẩm", "04_products"], ["Mã Giảm Giá", "05_coupons"], ["Đơn hàng", "06_orders"], ["Người dùng", "07_users"]];
for (const [n, f] of screens) { await run(H + `await go(${JSON.stringify(n)});top0();return 1`); await shot(`PF-2_${f}.png`); }

// ---------- categories ----------
R.categories = await run(H + `await go('Danh mục');const ci=document.querySelector('input');const c0=(await api('/categories')).length;
sv(ci,'');B('Thêm mới').click();await sleep(900);sv(ci,'   ');B('Thêm mới').click();await sleep(900);const blank=(await api('/categories')).length-c0;
sv(ci,'QA Test DM');B('Thêm mới').click();B('Thêm mới').click();await sleep(1200);const dbl=(await api('/categories')).filter(c=>c.name==='QA Test DM').length;const reset=ci.value==='';const okDlg=[...__dlg];__dlg.length=0;
[...document.querySelectorAll('tbody tr')].at(-1).querySelector('button').click();await sleep(900);const del={dlg:[...__dlg],removedWithoutConfirm:(await api('/categories')).filter(c=>c.name==='QA Test DM').length===1};__dlg.length=0;
return {blankCreated:blank,doubleSubmit:dbl,reset,successFeedback:okDlg,del}`);
await shot("PF-2_08_categories_blank_duplicate.png");
// keyboard Tab order + hover on the categories screen
await run(H + `document.activeElement.blur();window.__seq=[];document.addEventListener('focusin',e=>window.__seq.push(e.target.tagName+':'+(e.target.placeholder||e.target.textContent.trim().slice(0,15))));return 1`);
await keys(TAB, TAB, TAB);
R.tabOrder = await run(`return window.__seq`);
await shot("PF-2_10_tab_order.png");
const btnPos = await run(H + `const r=B('Thêm mới').getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2}`);
await hover(btnPos.x, btnPos.y);
R.hover = await run(H + `const b=B('Thêm mới');return {hovered:b.matches(':hover'),bg:getComputedStyle(b).backgroundColor}`);
// Enter submits
await run(H + `const i=document.querySelector('input');i.focus();sv(i,'QA Enter DM');return 1`);
await keys(ENTER); await sleep(1000);
R.enterSubmits = await run(`return document.body.innerText.includes('QA Enter DM')`);

// ---------- products ----------
R.products = await run(H + `await go('Sản phẩm');const q=s=>document.querySelector(s);const prods=async()=>(await (await fetch('http://localhost:3000/api/products')).json());
const nm=q('input[placeholder="Tên sản phẩm"]'),pr=q('input[placeholder="Giá tiền"]');const b=(await prods()).length;
sv(nm,'');sv(pr,'1000');B('Lưu sản phẩm').click();await sleep(800);const emptyName={created:(await prods()).length-b,msg:nm.validationMessage};
for(const [n,p] of [['QA SP gia rong',''],['QA SP gia 0','0'],['QA SP gia am','-1000'],['X'.repeat(300),'1000']]){sv(nm,n);sv(pr,p);B('Lưu sản phẩm').click();await sleep(900)}
const after=await prods();const o={emptyName,invalidCreated:after.length-b,longSaved:after.at(-1).name.length,selectPlaceholder:[...q('select').options].some(x=>!x.value)};
const r1=[...document.querySelectorAll('tbody tr')][1];r1.querySelectorAll('button')[0].click();await sleep(300);o.cancel={had:!!B('Hủy sửa')};B('Hủy sửa').click();await sleep(300);o.cancel.title=q('form h3').textContent;o.cancel.name=nm.value;
const row=[...document.querySelectorAll('tbody tr')].find(r=>r.innerText.includes('QA SP gia am'));row.scrollIntoView();await sleep(300);row.querySelectorAll('button')[0].click();await sleep(400);
const fr=q('form h3').getBoundingClientRect();o.formInView=fr.top>=0&&fr.bottom<=innerHeight;sv(nm,'QA SP da sua');B('Lưu sản phẩm').click();await sleep(1000);
o.editDlg=[...__dlg];__dlg.length=0;o.tableNames=[...new Set([...document.querySelectorAll('tbody tr')].map(r=>r.children[1].innerText))];o.dbRenamed=(await prods()).filter(p=>p.name==='QA SP da sua').length;
o.imgs=[...document.querySelectorAll('tbody img')].slice(0,2).map(i=>i.alt+':'+i.naturalWidth+'x'+i.naturalHeight);document.querySelector('table').scrollIntoView();return o`);
await shot("PF-2_09_products_edit_renames_all.png");

// ---------- coupons ----------
R.coupons = await run(H + `await go('Mã Giảm Giá');const [code,type,val,min,exp,maxu]=[...document.querySelectorAll('form input, form select')];const o={};
const list=async()=>api('/coupons');
const t=async(l,v)=>{__dlg.length=0;const b=(await list()).length;sv(code,v.code);sv(type,'percent');sv(val,v.val);sv(min,v.min??'0');sv(exp,v.exp||'2099-12-31');sv(maxu,v.maxu??'1');o[l+'_shown']=code.value;B('Tạo mã').click();await sleep(1000);o[l]={created:(await list()).length-b,dlg:[...__dlg],msg:[val,maxu].map(i=>i.validationMessage).filter(Boolean)}};
await t('lower',{code:'qatest1',val:'10'});await t('val0',{code:'QAZERO',val:'0'});await t('pct150',{code:'QA150',val:'150'});await t('minNeg',{code:'QAMINNEG',val:'10',min:'-5'});await t('maxu0',{code:'QAMAX0',val:'10',maxu:'0'});await t('past',{code:'QAPAST',val:'10',exp:'2020-01-01'});await t('dup',{code:'SAVE10',val:'10'});
o.typeNumberAcceptsText=(()=>{sv(val,'abc');return val.value})();document.querySelector('table').scrollIntoView();return o`);
await shot("PF-2_11_coupons_invalid.png");

// ---------- CSV import ----------
R.csv = await run(H + `await go('Sản phẩm');const fi=document.querySelector('input[type=file]');const imp=()=>[...document.querySelectorAll('button')].find(b=>/import/i.test(b.textContent));
const setF=async(n,t)=>{const dt=new DataTransfer();dt.items.add(new File([t],n));fi.files=dt.files;fi.dispatchEvent(new Event('change',{bubbles:true}));await sleep(500)};
const cnt=async()=>(await (await fetch('http://localhost:3000/api/products')).json()).length;
const o={initDisabled:imp().disabled,accept:fi.accept,tplHeaderOk:document.querySelector('a[download]').getAttribute('href').includes('name,price,description,imageUrl,category_id')};
await setF('data.txt','name,price\\nQA txt,1000');o.txtButton=imp().textContent;
await setF('rollback.csv','name,price,description,imageUrl,category_id\\nQA Good Row,100000,ok,,1\\nQA Bad Row,-5,bad,,1');const b=await cnt();imp().click();await sleep(1500);o.result=document.querySelector('.bg-green-100,.bg-red-100')?.innerText;o.added=(await cnt())-b;top0();return o`);
await shot("PF-2_12_csv_no_rollback.png");
R.csvQuoted = await run(H + `const fi=document.querySelector('input[type=file]');const dt=new DataTransfer();dt.items.add(new File(['name,price,description,imageUrl,category_id\\n"QA Ao, quan",150000,"Mo ta, co dau phay",,1'],'quoted.csv'));fi.files=dt.files;fi.dispatchEvent(new Event('change',{bubbles:true}));await sleep(600);
return [...[...document.querySelectorAll('table')][0].querySelectorAll('tbody td')].map(t=>t.textContent)`);
await shot("PF-2_13_csv_quoted_split.png");

// ---------- orders: XSS, reload, cancel, complete, revenue, history ----------
R.xssOrder = await run(H + `const u=await (await fetch('http://localhost:3000/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:'test@eshop.com',password:'Test1234!'})})).json();
const o=await (await fetch('http://localhost:3000/api/checkout',{method:'POST',headers:{'Content-Type':'application/json',Authorization:'Bearer '+u.token},body:JSON.stringify({total_amount:4000000,shipping_address:'<b>QA dia chi in dam</b><img src=x onerror="window.__xss=1">'})})).json();await go('Đơn hàng');return o.orderId`);
await nav(APP);
R.orders = await run(H + `const afterReload=document.querySelector('.flex-1 h2').textContent;await go('Đơn hàng');await sleep(300);const row=[...document.querySelectorAll('tbody tr')].find(r=>r.innerText.startsWith('#7'));
return {afterReload,bold:!!row.querySelector('td b'),img:!!row.querySelector('td img'),xss:window.__xss===1,statusLabels:[...document.querySelectorAll('tbody td span')].map(s=>s.textContent+'='+getComputedStyle(s).backgroundColor)}`);
await shot("PF-2_14_orders_xss.png");
R.orderActions = await run(H + `const rowOf=id=>[...document.querySelectorAll('tbody tr')].find(r=>r.innerText.startsWith('#'+id));__dlg.length=0;
[...rowOf(7).querySelectorAll('button')].find(b=>b.textContent.trim()==='Hủy').click();await sleep(1000);const o={cancelDlg:[...__dlg],s7:rowOf(7).children[4].innerText};
[...rowOf(4).querySelectorAll('button')].find(b=>b.textContent.trim()==='Hoàn thành').click();await sleep(1000);o.s4=rowOf(4).children[4].innerText;
const h0=history.length;for(const n of ['Sản phẩm','Danh mục','Dashboard']){await go(n)}o.historyGrowth=history.length-h0;o.url=location.href;o.revenue=document.querySelector('.text-green-600').textContent;return o`);
await shot("PF-2_15_dashboard_x2.png");

// ---------- users ----------
R.usersSelectAll = await run(H + `await go('Người dùng');const all=document.querySelector('thead input[type=checkbox]');all.click();await sleep(200);const c=[...document.querySelectorAll('tbody input[type=checkbox]')].map(x=>x.checked);all.click();return c`);

// ---------- long table ----------
R.longTable = await run(H + `await go('Sản phẩm');const fi=document.querySelector('input[type=file]');const rows=Array.from({length:25},(_,i)=>'QA Bulk '+(i+1)+','+((i+1)*10000)+',bulk,,3').join('\\n');
const dt=new DataTransfer();dt.items.add(new File(['name,price,description,imageUrl,category_id\\n'+rows],'bulk.csv'));fi.files=dt.files;fi.dispatchEvent(new Event('change',{bubbles:true}));await sleep(500);
[...document.querySelectorAll('button')].find(b=>b.textContent.startsWith('Import')).click();await sleep(1500);const m=document.querySelector('.flex-1');m.scrollTop=m.scrollHeight;await sleep(300);
const th=[...document.querySelectorAll('table')].at(-1).querySelector('thead');const r=th.getBoundingClientRect();return {rows:[...document.querySelectorAll('table')].at(-1).querySelectorAll('tbody tr').length,pos:getComputedStyle(th).position,theadVisible:r.bottom>0&&r.top<innerHeight}`);
await shot("PF-2_18_long_table.png");

// ---------- self delete (destructive, last) + logout ----------
await nav(APP);
R.selfDelete = await run(H + `await go('Người dùng');await sleep(300);const row=[...document.querySelectorAll('tbody tr')].find(r=>r.innerText.includes('admin@eshop.com'));const dis=row.querySelector('button').disabled;row.querySelector('button').click();await sleep(1200);
return {disabled:dis,dlg:[...__dlg],rows:[...document.querySelectorAll('tbody tr')].map(r=>r.innerText.replace(/\\s+/g,' '))}`);
await shot("PF-2_17_users_self_deleted.png");
R.logout = await run(H + `[...document.querySelectorAll('li')].find(l=>l.textContent.trim()==='Đăng xuất').click();await sleep(500);return {login:!!document.querySelector('input[type=password]'),token:localStorage.adminToken||null}`);
await cmd("browsingContext.traverseHistory", { context: ctx, delta: -1 }).catch((e) => (R.backAfterLogout = String(e.message)));
await sleep(1500);
R.afterBack = await run(`return {url:location.href,loginShown:!!document.querySelector('input[type=password]'),adminData:!!document.querySelector('tbody')}`);

writeFileSync(join(ROOT, "task3-cross-browser", "pf2-results.json"), JSON.stringify(R, null, 2));
console.log(JSON.stringify(R, null, 1));
await cmd("session.end").catch(() => {});
ff.kill();
await sleep(1000);
try { rmSync(profile, { recursive: true, force: true }); } catch {}
