"""Append the 5 'AI missed' candidate items (GUI-80..84) to the Task 1 workbook, then regenerate checklist.md.

Measured 2026-11-15 on Chromium, http://localhost:5174 (DOM probes, 640px viewport = 200% zoom of 1280px,
prefers-color-scheme: dark emulation). Source is marked as AI-drafted: the student must review/edit them and
write their own 'why the AI missed it' reasoning before submitting.
Usage: python tools/add_extra_items.py
"""
import sys
from copy import copy
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
SRC = "Human review (AI-drafted, SV cần duyệt)"
SHOT_DIR = "screenshots/"
ITEMS = [
    ("GUI-80", "IA-01", "Tất cả", "Tiêu đề tab trình duyệt mô tả đúng từng màn hình",
     "Tab hiện 'EShop Admin — Đơn hàng' (khác nhau theo màn hình), không phải tên dự án mặc định", "WCAG 2.4.2",
     "Prompt chỉ nhắc 'thẻ h1', AI không nghĩ tới <title>; thuộc phần metadata không nằm trong khung nhìn.",
     "Failed", "document.title = 'frontend-admin' ở cả 6 màn hình (đo bằng DOM, tên tab không nằm trong ảnh chụp trang).", ""),
    ("GUI-81", "IA-01", "Tất cả", "Thuộc tính lang của trang khớp ngôn ngữ giao diện",
     "<html lang=\"vi\"> vì giao diện tiếng Việt", "WCAG 3.1.1",
     "Mục này là markup ẩn; AI chỉ kiểm tra thứ nhìn thấy được trong giao diện và code React, không đọc index.html.",
     "Failed", "document.documentElement.lang = 'en' trong khi toàn bộ giao diện tiếng Việt (đo bằng DOM).", ""),
    ("GUI-82", "IA-01", "Tất cả", "Chế độ tối (prefers-color-scheme: dark) không làm hỏng hiển thị",
     "Giao diện có theme tối hoặc ít nhất khai báo color-scheme; chữ/nền vẫn đọc được", "Đề bài (ví dụ AI hay bỏ sót)",
     "Đề bài nêu sẵn dark mode là điểm AI hay quên; prompt gốc không yêu cầu theme.",
     "Failed", "Bật dark mode: trang vẫn nền sáng, không có @media (prefers-color-scheme: dark), color-scheme = normal — không hỗ trợ.", "extra_dark_mode_not_supported.jpg"),
    ("GUI-83", "IA-01", "Tất cả", "Bố cục dùng được khi thu nhỏ còn 640px (tương đương zoom 200% ở 1280px)",
     "Nội dung và nút thao tác vẫn truy cập được, không phải cuộn ngang mới thấy cột Hành động", "WCAG 1.4.4 / 1.4.10",
     "AI chỉ kiểm tra ở kích thước desktop mặc định; prompt không nêu zoom hay responsive.",
     "Failed", "Sidebar cố định 256px chiếm 40% chiều rộng; bảng Đơn hàng có 2 cột (Trạng thái, Hành động) nằm ngoài khung nhìn, phải cuộn ngang.", "extra_narrow_640px_layout.jpg"),
    ("GUI-84", "IA-03", "Tất cả", "Có landmark ngữ nghĩa (nav, main, header) cho trình đọc màn hình",
     "Sidebar nằm trong <nav>, nội dung trong <main>", "WCAG 1.3.1 / 2.4.1",
     "Giao diện nhìn đúng nên AI không thấy vấn đề; cần xem cây DOM/accessibility mới phát hiện.",
     "Failed", "Số thẻ <nav> = 0, <main> = 0, <header> = 0, phần tử có role = 0; menu là <li onClick> (đo bằng DOM).", ""),
]

path = ROOT / "task1-gui-checklist" / "GUI_Checklist_G5_Admin.xlsx"
wb = load_workbook(path)
ws = wb["Checklist"]
existing = {ws.cell(r, 1).value for r in range(2, ws.max_row + 1)}
tmpl = ws.max_row
for gid, ia, screen, item, expected, ref, why, status, notes, shot in ITEMS:
    if gid in existing:
        continue
    r = ws.max_row + 1
    for c, v in enumerate([gid, ia, screen, item, expected, ref, SRC, why, status, notes, SHOT_DIR + shot if shot else "(đo bằng DOM)"], 1):
        cell = ws.cell(r, c, v)
        src = ws.cell(tmpl, c)
        cell.font, cell.alignment, cell.border, cell.fill = copy(src.font), copy(src.alignment), copy(src.border), copy(src.fill)
wb.save(path)

import apply_results  # regenerates checklist.md from the workbook (RESULTS for GUI-01..79 are re-applied unchanged)
apply_results.main()
