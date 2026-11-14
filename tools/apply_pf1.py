"""Fill the PF-1 (Chrome 157 / Windows 11) column of the cross-platform matrix.

Run 2026-11-14 in the user's real Chrome via Claude in Chrome, viewport 1536x730, same seed data.
Every item gave the same result as the Task 1 run (Chromium), so statuses are copied from the checklist
and each Failed item gets the matching PF-1 screenshot (with the student-info overlay).
Usage: python tools/apply_pf1.py
"""
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "task1-gui-checklist" / "GUI_Checklist_G5_Admin.xlsx"
MATRIX = ROOT / "task3-cross-browser" / "cross_platform_matrix.xlsx"
SHOT = {  # Task 1 evidence -> PF-1 evidence
    "login_screen.jpg": "PF-1_01_login.jpg",
    "categories_tab-order.jpg": "PF-1_10_tab_order.jpg",
    "categories_blank_and_duplicate.jpg": "PF-1_08_categories_blank_duplicate.jpg",
    "products_edit_renames_all.jpg": "PF-1_09_products_edit_renames_all.jpg",
    "coupons_invalid_values.jpg": "PF-1_11_coupons_invalid.jpg",
    "csv_no_rollback.jpg": "PF-1_12_csv_no_rollback.jpg",
    "csv_quoted_comma_split.jpg": "PF-1_13_csv_quoted_split.jpg",
    "orders_xss_and_invalid_actions.jpg": "PF-1_14_orders_xss.jpg",
    "dashboard_revenue_x2.jpg": "PF-1_15_dashboard_x2.jpg",
    "backend_down_no_loading_empty_state.jpg": "PF-1_16_backend_down.jpg",
    "users_admin_deleted_self.jpg": "PF-1_17_users_self_deleted.jpg",
    "products_long_table_no_pagination.jpg": "PF-1_18_long_table.jpg",
}

src = {r[0]: (r[8], r[10]) for r in load_workbook(CHECK)["Checklist"].iter_rows(min_row=2, values_only=True) if r[0]}
wb = load_workbook(MATRIX)
ws = wb["Matrix"]
done = 0
for r in range(2, ws.max_row + 1):
    status, shot = src.get(ws.cell(r, 1).value, (None, None))
    if not status:
        continue  # human-added rows not executed on Chromium yet
    ws.cell(r, 6).value = status
    ws.cell(r, 9).value = "PF-1: giống kết quả Chromium (Task 1)."
    if status == "Failed":
        pf = SHOT[Path(shot).name]
        assert (MATRIX.parent / "screenshots" / "PF-1" / pf).exists(), pf
        ws.cell(r, 10).value = f"screenshots/PF-1/{pf}"
    done += 1
wb.save(MATRIX)
print(f"PF-1 filled for {done} items")
