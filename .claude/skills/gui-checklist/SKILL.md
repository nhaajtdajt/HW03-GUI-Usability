---
name: gui-checklist
description: Design and execute a GUI checklist (IA-01 general UI, IA-02 forms, IA-03 navigation, IA-04 feedback/state) for one or more screens of a web app, record Passed/Failed with notes and screenshots in Excel + Markdown, and turn failures into bug reports. Use when asked to "make a GUI checklist", "test the UI of screen X", or reuse HW03 Task 1 on another screen.
---

# GUI checklist — design → execute → bugs

Reusable version of HW03 Task 1. Works on any web screen the agent can open in a browser tool.

## Inputs to ask for (only if missing)
- App URL(s) and login (test account from the project's seed/README — never a real password).
- Screens in scope and the requirement source (spec file, FR codes).
- Output folder (default `task1-gui-checklist/`).

## Step 1 — Read the requirements first, not the code
1. Read the spec: collect every UI requirement (language, colours, currency, headings, required markers, input types, error position, step indicators, navbar highlight, breadcrumb, logout label, toast/confirm/empty state, alt text) and the functional rules of the screens in scope (validation limits, state machines).
2. Open each screen and list its forms, tables, buttons, dialogs.

## Step 2 — Design items (> 40, no duplicates)
- One row per checkable behaviour: `ID | IA | Screen | Checklist item | Expected result | Reference | Source | Why AI missed it | Status | Notes | Screenshot`.
- Cover all four IA groups. Make *Expected result* observable (what you would see), cite the FR or "General"/WCAG.
- Always consider the groups AI checklists usually miss: keyboard-only use and focus, contrast, zoom 200%, dark mode, RTL/long text, browser Back/F5/deep links, double submit, offline/error states, permission edge cases (delete self).
- Generate the workbook with `python tools/build_checklist.py` (edit `ITEMS`). Mark Source = `AI (...)`; the human reviewer adds rows with Source = `Human` and fills *Why AI missed it*.

## Step 3 — Execute
Use the browser tool; prefer DOM/JS inspection for measurable items and real clicks/keys for behaviour.
- Before testing destructive actions, back up the database file (or confirm the backend reseeds on restart).
- Replace `window.alert/confirm` with a logger so native dialogs become readable (`confirm` returns false so nothing is deleted by accident):
  ```js
  window.__dlg=[]; window.alert=m=>__dlg.push('alert: '+m); window.confirm=m=>{__dlg.push('confirm: '+m);return false}
  ```
- Set React-controlled inputs with the native setter + `input` event; upload files with `DataTransfer` on `input[type=file]`.
- Useful measurements: count `h1`, `input.type`, `label` count, `required/min/maxLength/accept`, button `getComputedStyle().backgroundColor` → contrast ratio (WCAG formula), Tab sequence via `focusin` listener, `history.length` after navigation, `scrollWidth > clientWidth` for overflow.
- Screenshot every Failed item (copy the tool's image file into `screenshots/` with a descriptive name). Login lockouts can trigger after wrong-password tests — test those last.
- Record results in `tools/apply_results.py` (`RESULTS = {n: (status, notes, screenshot)}`) and run it; it refuses a Failed item without a screenshot and regenerates `checklist.md`.

## Step 4 — Bugs
- Group Failed items by root cause into `bug-report.md`: summary table (ID, title, severity, checklist IDs) then one section per bug with Severity, screen, spec reference, steps, expected, actual, screenshot link.
- Severity: Critical = data loss/security, High = wrong business result or blocks main task, Medium = spec violation with workaround, Low = cosmetic/consistency.
- Post to GitHub Issues only after the user names the repository and approves; push screenshots to the repo and embed them by URL.

## Step 5 — Commit
One git commit per step: design, execution, bug logging.
