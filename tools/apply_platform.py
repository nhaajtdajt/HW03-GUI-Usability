"""Fill one platform column of the cross-platform matrix from a run that matched the Task 1 baseline.

PF-1: Chrome 157 / Windows 11, 2026-11-14, user's real Chrome via Claude in Chrome (viewport 1536x730).
PF-2: Firefox 160 / Windows 11, 2026-11-14, tools/firefox-pf2.mjs over WebDriver BiDi (window 1536x860);
      raw probe output in task3-cross-browser/pf2-results*.json.
Both runs gave the same Passed/Failed as Task 1 for every item, so statuses are copied from the checklist
and each Failed item points at that platform's screenshot (student-info overlay included).
Usage: python tools/apply_platform.py PF-1|PF-2 ["difference note"]
"""
import sys
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "task1-gui-checklist" / "GUI_Checklist_G5_Admin.xlsx"
MATRIX = ROOT / "task3-cross-browser" / "cross_platform_matrix.xlsx"
COL = {"PF-1": 6, "PF-2": 7, "PF-3": 8}
SUFFIX = {  # Task 1 evidence -> screenshot suffix used by every platform run
    "login_screen.jpg": "01_login",
    "categories_tab-order.jpg": "10_tab_order",
    "categories_blank_and_duplicate.jpg": "08_categories_blank_duplicate",
    "products_edit_renames_all.jpg": "09_products_edit_renames_all",
    "coupons_invalid_values.jpg": "11_coupons_invalid",
    "csv_no_rollback.jpg": "12_csv_no_rollback",
    "csv_quoted_comma_split.jpg": "13_csv_quoted_split",
    "orders_xss_and_invalid_actions.jpg": "14_orders_xss",
    "dashboard_revenue_x2.jpg": "15_dashboard_x2",
    "backend_down_no_loading_empty_state.jpg": "16_backend_down",
    "users_admin_deleted_self.jpg": "17_users_self_deleted",
    "products_long_table_no_pagination.jpg": "18_long_table",
}

pf = sys.argv[1]
note = sys.argv[2] if len(sys.argv) > 2 else f"{pf}: giống kết quả Task 1."
shots = {p.stem.split("_", 1)[1]: p.name for p in (MATRIX.parent / "screenshots" / pf).glob(f"{pf}_*")}
src = {r[0]: (r[8], r[10]) for r in load_workbook(CHECK)["Checklist"].iter_rows(min_row=2, values_only=True) if r[0]}
wb = load_workbook(MATRIX)
ws = wb["Matrix"]
done = 0
for r in range(2, ws.max_row + 1):
    status, shot = src.get(ws.cell(r, 1).value, (None, None))
    if not status:
        continue  # human-added rows not executed yet
    ws.cell(r, COL[pf]).value = status
    old = ws.cell(r, 9).value or ""
    ws.cell(r, 9).value = (old + "\n" if old and pf not in old else "") + note if pf not in old else old
    if status == "Failed":
        name = shots[SUFFIX[Path(shot).name]]
        prev = ws.cell(r, 10).value or ""
        if name not in prev:
            ws.cell(r, 10).value = (prev + "\n" if prev else "") + f"screenshots/{pf}/{name}"
    done += 1
wb.save(MATRIX)
print(f"{pf} filled for {done} items")
