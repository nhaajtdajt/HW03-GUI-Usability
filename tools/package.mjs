// Final packaging for Moodle: Markdown -> PDF (headless Chrome), git-log.txt, and
// <StudentID>_HW03_AI_GUIUsability_<grade>.zip one folder above the repo.
// Setup once: npm install --prefix tools marked@15.0.7
// Usage:      node tools/package.mjs <self-assessed grade 0-100>
import { readFileSync, writeFileSync, unlinkSync, existsSync, mkdirSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { marked } from "marked";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const STUDENT_ID = "23120231";
const grade = Number(process.argv[2]);
if (!Number.isInteger(grade) || grade < 0 || grade > 100) throw new Error("usage: node tools/package.mjs <grade 0-100>");

const CHROME = ["C:/Program Files/Google/Chrome/Application/chrome.exe",
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"].find(existsSync);
if (!CHROME) throw new Error("Chrome/Edge not found");

const CSS = `body{font-family:Arial,sans-serif;font-size:11pt;line-height:1.45;margin:0 8mm;color:#111}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:9pt}th,td{border:1px solid #bbb;padding:4px 6px;vertical-align:top}
th{background:#1f4e78;color:#fff}code{background:#f2f2f2;padding:1px 3px;font-size:9pt}pre{background:#f2f2f2;padding:8px;white-space:pre-wrap}
blockquote{border-left:4px solid #f0b400;margin:8px 0;padding:4px 10px;background:#fff8e1}h1,h2{color:#1f4e78}img{max-width:100%}`;

const PDFS = ["report.md", "ai/ai-audit-report.md", "ai/ai-critique.md", "task1-gui-checklist/bug-report.md", "task2-usability/07-analysis.md"];
mkdirSync(join(ROOT, "pdf"), { recursive: true });
for (const md of PDFS) {
  const src = join(ROOT, md);
  const html = src.replace(/\.md$/, ".print.html"); // next to the .md so relative image links resolve
  writeFileSync(html, `<!doctype html><meta charset="utf-8"><style>${CSS}</style>${marked.parse(readFileSync(src, "utf8"))}`);
  const out = join(ROOT, "pdf", md.replace(/\//g, "_").replace(/\.md$/, ".pdf"));
  execFileSync(CHROME, ["--headless=new", "--disable-gpu", "--no-pdf-header-footer", `--print-to-pdf=${out}`, pathToFileURL(html).href], { stdio: "ignore" });
  unlinkSync(html);
  if (!existsSync(out)) throw new Error(`PDF not produced: ${out}`);
  console.log("pdf", out);
}

writeFileSync(join(ROOT, "git-log.txt"), execFileSync("git", ["-C", ROOT, "log", "--stat", "--date=iso"], { encoding: "utf8" }));
console.log("git-log.txt written");

const zip = resolve(ROOT, "..", `${STUDENT_ID}_HW03_AI_GUIUsability_${String(grade).padStart(3, "0")}.zip`);
// Windows bsdtar writes a real .zip with -a; the SUT clone and dependencies are not part of the submission.
execFileSync("C:/Windows/System32/tar.exe", ["-a", "-cf", zip, "--exclude=eshop-sut", "--exclude=node_modules",
  "--exclude=.git", "--exclude=__pycache__", "--exclude=*.zip", "-C", ROOT, "."], { stdio: "inherit" });
console.log("zip", zip);
