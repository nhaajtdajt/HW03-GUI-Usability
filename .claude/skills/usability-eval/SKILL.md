---
name: usability-eval
description: Plan, run and analyse a small moderated usability evaluation (think-aloud, 5–8 participants, SUS or UEQ-S) for one end-to-end flow of an app — produces objectives, goal-based task scenario, moderator script, probe questions, observation templates, participant table, SUS/task metrics workbook, then the severity-ranked findings report. Use when asked to "do a usability test", "prepare SUS", "analyse usability sessions", or reuse HW03 Task 2 on another flow.
---

# Usability evaluation — plan → sessions → analysis

Reusable version of HW03 Task 2. The agent prepares and analyses; **real people run the sessions** — never invent participants, quotes, timings or SUS answers.

## Phase 1 — Plan & prepare (agent drafts, human reviews)
1. Ask for: the flow (start → end screen), target user profile, number of participants, language, session format (in person / remote).
2. Walk the flow yourself in the browser and note the data each task needs (accounts, seed data, reset procedure). Write a reset step so every session starts identical.
3. Write in `task2-usability/`:
   - `01-plan.md` — objectives as research questions → metric for each; target profile; method; task table (scenario text, success criterion, time limit); instruments; metrics; pilot; ethics/privacy (mask 4 middle digits of phone numbers).
   - `02-session-script.md` — setup checklist, intro text (testing the product not the person, think-aloud, consent to record), neutral prompts, when to assist, close; probe questions covering at least **clarity, error recovery, speed, trust**.
   - `03-task-cards.md` — printable goal-based cards (what to achieve, never which buttons to press) + SUS form in the participants' language.
   - `04-observation-template.md`, `05-participants.md`, `06-pilot-notes.md`.
   - Metrics workbook: `python tools/build_sus_sheet.py` (SUS score = Σ(odd−1) + Σ(5−even) × 2.5, completion S/P/F, time, errors, assists — all formulas).
4. Scenario rules: realistic goal with concrete values; one task per card; do not reveal menu names used by the UI; include a trust check on any number the UI computes.

## Phase 2 — Sessions (human)
Remind the tester: reset data, record screen + audio with consent, observe neutrally, structured notes with video timestamps (M friction / E error / Q quote / B bug / + positive), SUS before probes.

## Phase 3 — Analyse (agent, from the filled notes only)
1. Read every `sessions/P*.md` and the workbook. Report SUS mean, median, min/max, SD, grade vs 68 benchmark; completion rate and mean time per task.
2. Affinity-group observations: same pain point seen in ≥ 2 participants → one finding; list participant IDs and timestamps as evidence.
3. Separate **isolated bugs** (system defect, reproducible) from **systemic design issues** (pattern across tasks/users).
4. Rate severity (Nielsen 0–4): 4 = blocks task completion, 3 = major delay/errors, 2 = minor, 1 = cosmetic. Rank findings; give a recommendation per finding.
5. Write `07-analysis.md`: method recap, participant summary, metrics tables, findings ranked by severity, bug list (with steps + screenshot for GitHub Issues), limitations (small sample, moderator effects).
6. One git commit per session note and one for the analysis.
