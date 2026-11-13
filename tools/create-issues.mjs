// Create one GitHub issue per "## BUG-xx" section of bug-report.md (screenshots embedded from the repo),
// then write the issue links back into the bug-report summary table. Requires `gh` logged in.
// Usage: node tools/create-issues.mjs <owner/repo> [branch]
import { readFileSync, writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";

const [repo, branch = "master"] = process.argv.slice(2);
if (!repo) throw new Error("usage: node tools/create-issues.mjs <owner/repo> [branch]");
const file = new URL("../task1-gui-checklist/bug-report.md", import.meta.url);
let md = readFileSync(file, "utf8").replace(/\r\n/g, "\n");
const env = md.match(/\*\*Môi trường:\*\*.*\n/)[0];
const raw = (p) => `https://github.com/${repo}/blob/${branch}/task1-gui-checklist/${p}?raw=true`;
const gh = (...a) => execFileSync("gh", a, { encoding: "utf8" }).trim();

const sevColor = { Critical: "b60205", High: "d93f0b", Medium: "fbca04", Low: "c2e0c6" };
for (const [s, c] of Object.entries(sevColor)) gh("label", "create", `severity:${s}`, "--color", c, "--force", "-R", repo);

const sections = md.split(/\n(?=## BUG-\d+)/).slice(1);
const links = {};
for (const sec of sections) {
  const [, id, title] = sec.match(/^## (BUG-\d+) — (.+)/);
  const sev = sec.match(/\*\*Severity:\*\* (\w+)/)[1];
  const shots = [...new Set([...sec.matchAll(/\]\((screenshots\/[^)]+)\)/g)].map((m) => m[1]))];
  const body = [
    sec.replace(/^## .+\n/, "").replace(/\]\((screenshots\/[^)]+)\)/g, (_, p) => `](${raw(p)})`).replace(/\n---\s*$/, "").trim(),
    "", env.trim(), "", "### Screenshot", ...shots.map((p) => `![${p}](${raw(p)})`),
  ].join("\n");
  const url = gh("issue", "create", "-R", repo, "--title", `[${id}] ${title}`, "--body", body, "--label", "bug", "--label", `severity:${sev}`);
  links[id] = url;
  console.log(id, url);
}
// add an Issue column to the summary table
md = md.replace(/\| Bug \| Tiêu đề \| Severity \| Checklist \|\n\|---\|---\|---\|---\|/, "| Bug | Tiêu đề | Severity | Checklist | GitHub Issue |\n|---|---|---|---|---|");
md = md.replace(/^\| (BUG-\d+) \|(.+)\|$/gm, (line, id) => (links[id] ? `${line} [#${links[id].split("/").pop()}](${links[id]}) |` : line));
writeFileSync(file, md);
console.log(`${Object.keys(links).length} issues created`);
