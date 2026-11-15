"""Build task2-usability/SUS_and_Task_Metrics.xlsx (input cells yellow, all results are formulas).
Usage: python tools/build_sus_sheet.py   (overwrites the file — run once, then fill it in Excel)
"""
import sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).resolve().parent.parent / (sys.argv[1] if len(sys.argv) > 1 else "task2-usability") / "SUS_and_Task_Metrics.xlsx"  # optional arg: output folder
PEOPLE = [f"P{i}" for i in range(1, 8)]
TASKS = sys.argv[2:7] if len(sys.argv) >= 7 else ["T1 Đăng nhập", "T2 Đọc thống kê", "T3 Tạo sản phẩm", "T4 Tạo mã giảm giá", "T5 Xử lý đơn"]  # optional: 5 task names
F = Font(name="Arial", size=10)
B = Font(name="Arial", size=10, bold=True)
H = Font(name="Arial", size=10, bold=True, color="FFFFFF")
HF = PatternFill("solid", fgColor="1F4E78")
IN = PatternFill("solid", fgColor="FFF2CC")
s = Side(style="thin", color="BFBFBF")
BD = Border(left=s, right=s, top=s, bottom=s)
C = Alignment(horizontal="center", vertical="center", wrap_text=True)


def head(ws, row, values):
    for col, v in enumerate(values, 1):
        c = ws.cell(row, col, v)
        c.font, c.fill, c.border, c.alignment = H, HF, BD, C


def box(ws, rng, font=F, fill=None):
    for row in ws[rng]:
        for c in row:
            c.font, c.border, c.alignment = font, BD, C
            if fill:
                c.fill = fill


wb = Workbook()
# ---------- SUS ----------
ws = wb.active
ws.title = "SUS"
head(ws, 1, ["Participant"] + [f"Q{i}" for i in range(1, 11)] + ["SUS score"])
for r, p in enumerate(PEOPLE, 2):
    ws.cell(r, 1, p)
    # odd items: score-1, even items: 5-score; x2.5 → 0..100. Blank until all 10 answers are entered.
    ws.cell(r, 12, f'=IF(COUNT(B{r}:K{r})=10,((B{r}-1)+(5-C{r})+(D{r}-1)+(5-E{r})+(F{r}-1)+(5-G{r})'
                   f'+(H{r}-1)+(5-I{r})+(J{r}-1)+(5-K{r}))*2.5,"")')
    ws.cell(r, 12).number_format = "0.0"
box(ws, "A2:L8")
box(ws, "B2:K8", fill=IN)
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True,
                    error="Nhập số nguyên từ 1 đến 5", showErrorMessage=True)
ws.add_data_validation(dv)
dv.add("B2:K8")
stats = [("Số phiếu", "=COUNT(L2:L8)", "0"),
         ("Trung bình", '=IFERROR(AVERAGE(L2:L8),"")', "0.0"),
         ("Trung vị", '=IFERROR(MEDIAN(L2:L8),"")', "0.0"),
         ("Thấp nhất", '=IFERROR(MIN(L2:L8),"")', "0.0"),
         ("Cao nhất", '=IFERROR(MAX(L2:L8),"")', "0.0"),
         ("Độ lệch chuẩn", '=IFERROR(STDEV(L2:L8),"")', "0.0"),
         ("Xếp loại (theo trung bình)", '=IF(L11="","",IF(L11>=80.3,"Xuất sắc (A)",IF(L11>=68,"Trên trung bình",IF(L11>=51,"Dưới trung bình","Kém"))))', "@")]
for i, (label, formula, fmt) in enumerate(stats, 10):
    ws.cell(i, 11, label).font = B
    c = ws.cell(i, 12, formula)
    c.font, c.number_format, c.border = B, fmt, BD
ws.cell(18, 1, "Công thức: câu lẻ (điểm − 1), câu chẵn (5 − điểm), tổng × 2,5. Ngưỡng 68 = trung bình ngành; "
               "80,3 = hạng A (Sauro & Lewis, Quantifying the User Experience, 2016).").font = Font(name="Arial", size=9, italic=True)
ws.cell(19, 1, "Ô nền vàng: nhập câu trả lời 1–5 từ phiếu SUS của từng người. Ví dụ phiếu 4,2,4,1,4,2,5,2,4,2 → 80,0 điểm.").font = Font(name="Arial", size=9, italic=True)
ws.column_dimensions["A"].width = 13
for col in "BCDEFGHIJK":
    ws.column_dimensions[col].width = 6
ws.column_dimensions["K"].width = 24
ws.column_dimensions["L"].width = 16

# ---------- Tasks ----------
t = wb.create_sheet("Tasks")
cols = ["Participant"]
for name in TASKS:
    cols += [f"{name}\nKết quả", f"{name}\nThời gian (s)", f"{name}\nSố lỗi", f"{name}\nTrợ giúp"]
head(t, 1, cols)
t.row_dimensions[1].height = 45
for r, p in enumerate(PEOPLE, 2):
    t.cell(r, 1, p)
box(t, "A2:U8")
box(t, "B2:U8", fill=IN)
res = DataValidation(type="list", formula1='"S,P,F"', allow_blank=True)
t.add_data_validation(res)
labels = ["Tỷ lệ thành công (S)", "Thành công kể cả P", "Thời gian TB (s)", "Lỗi TB", "Tổng trợ giúp"]
for i, label in enumerate(labels, 10):
    t.cell(i, 1, label).font = B
for k in range(len(TASKS)):
    rc, tc, ec, ac = (2 + 4 * k + j for j in range(4))
    L = lambda c: t.cell(1, c).column_letter
    res.add(f"{L(rc)}2:{L(rc)}8")
    n = f"COUNTA({L(rc)}2:{L(rc)}8)"
    t.cell(10, rc, f'=IF({n}=0,"",COUNTIF({L(rc)}2:{L(rc)}8,"S")/{n})').number_format = "0%"
    t.cell(11, rc, f'=IF({n}=0,"",(COUNTIF({L(rc)}2:{L(rc)}8,"S")+COUNTIF({L(rc)}2:{L(rc)}8,"P"))/{n})').number_format = "0%"
    t.cell(12, tc, f'=IFERROR(AVERAGE({L(tc)}2:{L(tc)}8),"")').number_format = "0"
    t.cell(13, ec, f'=IFERROR(AVERAGE({L(ec)}2:{L(ec)}8),"")').number_format = "0.0"
    t.cell(14, ac, f"=SUM({L(ac)}2:{L(ac)}8)")
for row in t.iter_rows(min_row=10, max_row=14):
    for c in row:
        c.font, c.border = B, BD
t.column_dimensions["A"].width = 22
for c in range(2, 22):
    t.column_dimensions[t.cell(1, c).column_letter].width = 11
t.cell(16, 1, "Kết quả: S = tự hoàn thành · P = hoàn thành sau gợi ý hoặc có sai nhỏ · F = không hoàn thành. Thời gian lấy từ video.").font = Font(name="Arial", size=9, italic=True)
t.freeze_panes = "B2"

OUT.parent.mkdir(exist_ok=True)
wb.save(OUT)
print("saved", OUT)
