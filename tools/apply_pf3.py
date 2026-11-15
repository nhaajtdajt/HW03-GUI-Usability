"""Fill the PF-3 column (Safari 16.5.1 / macOS, BrowserStack Live free trial) of the cross-platform matrix.

Only what the two screenshots in task3-cross-browser/screenshots/PF-3 prove is graded; every other item is N/A
because the trial gives one 1-minute session per browser version and the remote keyboard drops Shift characters
('@' -> '2'), so logging in again inside the minute was not possible.
Usage: python tools/apply_pf3.py
"""
from pathlib import Path
from openpyxl import load_workbook

MATRIX = Path(__file__).resolve().parent.parent / "task3-cross-browser" / "cross_platform_matrix.xlsx"
LOGIN, ALERT = "screenshots/PF-3/PF-3_01_login.jpg", "screenshots/PF-3/PF-3_02_login_alert.jpg"
GRADED = {  # id: (status, shot, note)
    "GUI-01": ("Failed", LOGIN, "Tiêu đề, placeholder và nút trang đăng nhập vẫn tiếng Anh."),
    "GUI-02": ("Failed", LOGIN, "'Admin Login', 'Password', 'Login'."),
    "GUI-20": ("Passed", None, "Ô mật khẩu hiển thị dấu chấm (type=password)."),
    "GUI-21": ("Failed", LOGIN, "Form đăng nhập chỉ có placeholder, không có nhãn."),
    "GUI-62": ("Failed", ALERT, "Safari hiện hộp alert() gốc 'Đăng nhập thất bại' — đây là ảnh duy nhất chụp được hộp alert."),
    "GUI-79": ("Failed", ALERT, "Lỗi đăng nhập hiện bằng alert(), không phải thông báo trên form."),
}
NA = "N/A: trial BrowserStack 1 phút/phiên bản trình duyệt; bàn phím từ xa mất ký tự Shift nên không đăng nhập lại kịp."

wb = load_workbook(MATRIX)
ws = wb["Matrix"]
for r in range(2, ws.max_row + 1):
    gid = ws.cell(r, 1).value
    if not gid:
        continue
    status, shot, note = GRADED.get(gid, ("N/A", None, NA))
    ws.cell(r, 8).value = status
    prev = ws.cell(r, 9).value or ""
    ws.cell(r, 9).value = (prev + "\n" if prev else "") + f"PF-3 (Safari 16.5.1 / macOS, BrowserStack): {note}"
    if shot:
        ws.cell(r, 10).value = ((ws.cell(r, 10).value or "") + "\n" if ws.cell(r, 10).value else "") + shot
wb.save(MATRIX)
print(f"PF-3: {sum(v[0] != 'N/A' for v in GRADED.values())} graded, {ws.max_row - 1 - len(GRADED)} N/A")
