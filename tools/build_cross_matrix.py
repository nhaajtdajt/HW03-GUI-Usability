"""Build task3-cross-browser/cross_platform_matrix.xlsx from the Task 1 workbook (all checklist rows,
including Human rows added later). Re-run after adding rows to the checklist; it overwrites the matrix.
Usage: python tools/build_cross_matrix.py
"""
from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "task1-gui-checklist" / "GUI_Checklist_G5_Admin.xlsx"
OUT = ROOT / "task3-cross-browser" / "cross_platform_matrix.xlsx"
PLATFORMS = ["PF-1 Chrome / Windows 11", "PF-2 Firefox / Windows", "PF-3 Safari / macOS (hoặc Chrome / Android)"]

s = Side(style="thin", color="BFBFBF")
BD = Border(left=s, right=s, top=s, bottom=s)
F, B = Font(name="Arial", size=10), Font(name="Arial", size=10, bold=True)
WRAP = Alignment(wrap_text=True, vertical="top")
IN = PatternFill("solid", fgColor="FFF2CC")

items = [r[:5] for r in load_workbook(SRC)["Checklist"].iter_rows(min_row=2, values_only=True) if r[0]]
wb = Workbook()
ws = wb.active
ws.title = "Matrix"
headers = ["ID", "IA", "Screen", "Checklist item", "Expected result"] + PLATFORMS + ["Khác biệt giữa nền tảng", "Screenshot"]
ws.append(headers)
for c in ws[1]:
    c.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="1F4E78")
    c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
    c.border = BD
for it in items:
    ws.append(list(it) + ["", "", "", "", ""])
last = ws.max_row
for row in ws.iter_rows(min_row=2, max_row=last):
    for c in row:
        c.font, c.alignment, c.border = F, WRAP, BD
    for c in row[5:10]:
        c.fill = IN
dv = DataValidation(type="list", formula1='"Passed,Failed,N/A"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"F2:H{last}")
for col, w in zip("ABCDEFGHIJ", [9, 8, 20, 42, 48, 14, 14, 18, 40, 28]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "F2"
ws.auto_filter.ref = f"A1:J{last}"

sm = wb.create_sheet("Summary")
sm.append(["Nền tảng", "Đã chạy", "Passed", "Failed", "N/A", "Tỷ lệ Passed"])
for c in sm[1]:
    c.font, c.border = B, BD
for i, (name, col) in enumerate(zip(PLATFORMS, "FGH"), 2):
    rng = f"Matrix!{col}2:{col}{last}"
    sm.append([name, f'=COUNTIF({rng},"Passed")+COUNTIF({rng},"Failed")', f'=COUNTIF({rng},"Passed")',
               f'=COUNTIF({rng},"Failed")', f'=COUNTIF({rng},"N/A")', f'=IF(B{i}=0,"",C{i}/B{i})'])
    sm.cell(i, 6).number_format = "0.0%"
    for c in sm[i]:
        c.font, c.border = F, BD
sm.append([])
sm.append(["Mục cho kết quả khác nhau giữa các nền tảng",
           f'=SUMPRODUCT((Matrix!F2:F{last}<>"")*(Matrix!G2:G{last}<>"")*(Matrix!H2:H{last}<>"")'
           f'*((Matrix!F2:F{last}<>Matrix!G2:G{last})+(Matrix!G2:G{last}<>Matrix!H2:H{last})>0))'])
sm["A7"].font = B
sm.column_dimensions["A"].width = 44
for col in "BCDEF":
    sm.column_dimensions[col].width = 13

OUT.parent.mkdir(exist_ok=True)
wb.save(OUT)
print(f"{len(items)} items x {len(PLATFORMS)} platforms -> {OUT}")
