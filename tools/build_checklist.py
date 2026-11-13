"""Build the Task 1 GUI checklist (Excel + Markdown) for EShop Web Admin (G5).

Run once to create the files; afterwards edit the .xlsx directly (Status / Notes / Screenshot,
and human-added rows with Source = "Human"). Re-running overwrites the .xlsx.
Usage: python tools/build_checklist.py
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).resolve().parent.parent / "task1-gui-checklist"
SRC = "AI (Claude Opus 5.5)"

# (IA, screen, item, expected, reference)
ITEMS = [
    # ---------------- IA-01 General UI standards ----------------
    ("IA-01", "Tất cả", "Ngôn ngữ giao diện thống nhất tiếng Việt", "Mọi nhãn, nút, tiêu đề, thông báo đều tiếng Việt (trừ thuật ngữ chuẩn như Dashboard, CSV)", "FR-21"),
    ("IA-01", "Admin Login", "Tiêu đề, placeholder và nút của form đăng nhập bằng tiếng Việt", "Hiển thị 'Đăng nhập quản trị', 'Mật khẩu', 'Đăng nhập' thay vì 'Admin Login', 'Password', 'Login'", "FR-21"),
    ("IA-01", "Tất cả", "Mỗi màn hình có đúng một thẻ <h1> mô tả nội dung trang", "Mỗi màn hình có 1 <h1> là tên màn hình (VD: 'Quản lý Sản phẩm'), không dùng <h1> cho logo", "FR-21"),
    ("IA-01", "Tất cả", "Nút hành động tích cực dùng màu xanh dương", "Các nút Thêm mới, Lưu sản phẩm, Tạo mã, Xác nhận, Import đều màu xanh dương", "FR-21"),
    ("IA-01", "Tất cả", "Nút nguy hiểm/hủy bỏ dùng màu đỏ", "Các nút Xóa, Hủy (đơn hàng) đều màu đỏ", "FR-21"),
    ("IA-01", "Tất cả", "Đơn vị tiền tệ thống nhất ký hiệu ₫ với phân cách hàng nghìn", "Mọi giá trị tiền dạng 1.000.000 ₫, cùng một kiểu dấu phân cách trên mọi màn hình", "FR-21"),
    ("IA-01", "Quản lý Sản phẩm", "Cột Giá trong bảng sản phẩm có phân cách hàng nghìn", "Giá hiển thị dạng 15.000.000 ₫, không phải 15000000 ₫", "FR-21"),
    ("IA-01", "Dashboard", "Nhãn thẻ thống kê rõ nghĩa, không trộn tiếng Anh", "Nhãn 'Tổng doanh thu (đơn đã giao)' thay vì '(Delivered)'", "FR-21"),
    ("IA-01", "Tất cả", "Font chữ, cỡ chữ và khoảng cách nhất quán giữa các màn hình", "Tiêu đề, bảng, form dùng cùng font và thang cỡ chữ ở mọi tab", "General"),
    ("IA-01", "Tất cả", "Tên menu khớp với tiêu đề màn hình tương ứng", "Menu 'Mã Giảm Giá' mở màn hình có tiêu đề tương ứng, viết hoa thống nhất", "General"),
    ("IA-01", "Tất cả", "Cách viết hoa tiêu đề cột bảng nhất quán", "Các cột cùng một kiểu (VD: 'Tên danh mục', không lẫn 'Tên Danh Mục' và 'Tên SP')", "General"),
    ("IA-01", "Tất cả", "Không dùng chữ viết tắt khó hiểu trên nhãn", "Dùng 'Tên sản phẩm' thay vì 'Tên SP'; nhãn 'Role' được Việt hóa", "General"),
    ("IA-01", "Tất cả", "Thứ tự Tab đi từ trên xuống dưới, trái sang phải", "Nhấn Tab lần lượt qua menu → tiêu đề → form → bảng theo thứ tự đọc", "FR-21"),
    ("IA-01", "Quản lý Sản phẩm", "Ảnh sản phẩm trong bảng có thuộc tính alt mô tả", "Mỗi <img> có alt khác rỗng mô tả sản phẩm", "FR-24"),
    ("IA-01", "Quản lý Sản phẩm", "Ảnh thu nhỏ giữ đúng tỷ lệ, không méo", "Ảnh 1:1, cắt/thu gọn không làm biến dạng", "FR-05"),
    ("IA-01", "Tất cả", "Độ tương phản chữ và nền đạt WCAG AA", "Tỷ lệ tương phản ≥ 4.5:1 cho chữ thường (kể cả menu trên nền tối)", "WCAG 2.1 1.4.3"),
    ("IA-01", "Tất cả", "Bố cục không vỡ ở độ rộng 1366px và 1024px", "Bảng, form, sidebar hiển thị đủ, không chồng lấn, không cuộn ngang trang", "General"),
    ("IA-01", "Quản lý Mã giảm giá", "Bảng coupon hiển thị loại và giá trị rõ ràng", "Loại 'Phần trăm/Cố định' và giá trị '10%' hoặc '50.000 ₫' đúng theo loại", "FR-17"),
    # ---------------- IA-02 Forms ----------------
    ("IA-02", "Admin Login", "Trường Email dùng type=\"email\"", "Nhập 'abc' rồi submit thì trình duyệt báo định dạng email không hợp lệ", "FR-22"),
    ("IA-02", "Admin Login", "Trường Mật khẩu dùng type=\"password\"", "Ký tự mật khẩu bị che", "FR-22"),
    ("IA-02", "Tất cả", "Mỗi trường nhập có nhãn (label) hiển thị, không chỉ placeholder", "Nhãn vẫn còn khi người dùng đã nhập dữ liệu", "General"),
    ("IA-02", "Tất cả", "Trường bắt buộc có dấu * bên cạnh nhãn", "Các trường bắt buộc (Tên SP, Giá, Danh mục, Mã coupon, Ngày hết hạn...) có *", "FR-22"),
    ("IA-02", "Quản lý Danh mục", "Không cho thêm danh mục với tên rỗng", "Bấm 'Thêm mới' khi để trống thì hiện lỗi, không tạo dòng mới", "FR-14"),
    ("IA-02", "Quản lý Danh mục", "Không cho thêm danh mục tên chỉ gồm khoảng trắng", "Nhập '   ' thì hiện lỗi, không tạo danh mục rỗng", "FR-14"),
    ("IA-02", "Quản lý Sản phẩm", "Tên sản phẩm là bắt buộc", "Để trống Tên thì không lưu được, có thông báo lỗi", "FR-15"),
    ("IA-02", "Quản lý Sản phẩm", "Tên sản phẩm tối đa 255 ký tự", "Không nhập được quá 255 ký tự hoặc có thông báo lỗi khi vượt", "FR-15"),
    ("IA-02", "Quản lý Sản phẩm", "Giá sản phẩm là bắt buộc", "Để trống Giá thì không lưu được, có thông báo lỗi", "FR-15"),
    ("IA-02", "Quản lý Sản phẩm", "Giá phải là số dương (> 0)", "Nhập 0 hoặc -1000 thì bị chặn với thông báo lỗi", "FR-15"),
    ("IA-02", "Quản lý Sản phẩm", "Danh mục bắt buộc chọn từ danh sách", "Dropdown có lựa chọn mặc định 'Chọn danh mục'; chưa chọn thì không lưu", "FR-15"),
    ("IA-02", "Quản lý Sản phẩm", "Bấm 'Sửa' đưa đúng dữ liệu sản phẩm lên form", "Form điền đủ tên, giá, ảnh, mô tả, danh mục; tiêu đề đổi thành 'Sửa sản phẩm'", "FR-15"),
    ("IA-02", "Quản lý Sản phẩm", "Nút 'Hủy sửa' đưa form về chế độ thêm mới", "Form trống, tiêu đề 'Thêm sản phẩm mới', nút 'Hủy sửa' biến mất", "FR-15"),
    ("IA-02", "Import CSV", "Chỉ chấp nhận file .csv", "Hộp chọn file lọc .csv; chọn file .xlsx/.txt thì hiện lỗi", "FR-16"),
    ("IA-02", "Import CSV", "Có link tải file mẫu với header đúng", "File mẫu có header name,price,description,imageUrl,category_id và hiển thị tiếng Việt đúng", "FR-16"),
    ("IA-02", "Import CSV", "Xem trước tách cột đúng với trường có dấu phẩy trong nháy kép", "Dòng có description \"Áo, quần\" hiển thị đúng 1 ô, không lệch cột (RFC 4180)", "FR-16"),
    ("IA-02", "Quản lý Mã giảm giá", "Mã coupon bắt buộc và tự chuyển chữ hoa", "Gõ 'save20' hiển thị 'SAVE20'; để trống thì không tạo được", "FR-17"),
    ("IA-02", "Quản lý Mã giảm giá", "Giá trị giảm phải là số dương", "Nhập 0 hoặc số âm thì bị chặn với thông báo lỗi", "FR-17"),
    ("IA-02", "Quản lý Mã giảm giá", "Giá trị phần trăm không vượt quá 100", "Loại Phần trăm, nhập 150 thì bị chặn", "FR-17 (logic)"),
    ("IA-02", "Quản lý Mã giảm giá", "Đơn tối thiểu ≥ 0", "Nhập số âm thì bị chặn", "FR-17"),
    ("IA-02", "Quản lý Mã giảm giá", "Số lần dùng tối đa/người ≥ 1", "Nhập 0 thì bị chặn", "FR-17"),
    ("IA-02", "Quản lý Mã giảm giá", "Không chọn được ngày hết hạn trong quá khứ", "Date picker chặn ngày trước hôm nay hoặc báo lỗi", "General"),
    ("IA-02", "Quản lý Mã giảm giá", "Mã coupon trùng bị từ chối với thông báo rõ", "Tạo lại 'SAVE10' thì hiện 'Mã đã tồn tại'", "FR-17"),
    ("IA-02", "Tất cả", "Thông báo lỗi validation xuất hiện phía trên nút submit", "Lỗi hiển thị inline trên nút submit, gần trường bị lỗi", "FR-22"),
    ("IA-02", "Tất cả", "Form được reset sau khi submit thành công", "Sau khi thêm danh mục/sản phẩm/coupon, các trường trở về trống/mặc định", "General"),
    ("IA-02", "Tất cả", "Nhấn Enter trong form sẽ submit", "Enter trong ô nhập thực hiện đúng hành động của form", "General"),
    # ---------------- IA-03 Navigation ----------------
    ("IA-03", "Sidebar", "Mục menu đang chọn được highlight", "Mục tương ứng màn hình hiện tại có màu/nền khác biệt rõ", "FR-23"),
    ("IA-03", "Sidebar", "Mục menu dùng được bằng bàn phím", "Tab tới được từng mục menu và Enter/Space mở màn hình", "FR-21"),
    ("IA-03", "Sidebar", "Nút đăng xuất có nhãn 'Đăng xuất'", "Nhãn đúng 'Đăng xuất', không phải 'Thoát'", "FR-23"),
    ("IA-03", "Sidebar", "Đăng xuất quay về màn hình đăng nhập và không vào lại bằng Back", "Sau đăng xuất, nhấn Back không hiển thị dữ liệu admin", "FR-12"),
    ("IA-03", "Tất cả", "Mỗi màn hình có URL riêng", "Mỗi tab đổi URL (VD: /products); copy URL mở đúng màn hình", "General"),
    ("IA-03", "Tất cả", "Tải lại trang giữ nguyên màn hình đang xem", "F5 ở 'Đơn hàng' vẫn ở 'Đơn hàng', không về Dashboard", "General"),
    ("IA-03", "Tất cả", "Nút Back của trình duyệt quay về màn hình trước", "Từ Sản phẩm sang Đơn hàng, nhấn Back thì về Sản phẩm", "General"),
    ("IA-03", "Tất cả", "Có breadcrumb hoặc chỉ dẫn vị trí ở màn hình con", "Hiển thị 'Admin / Quản lý Sản phẩm' hoặc tương đương", "FR-23"),
    ("IA-03", "Admin Login", "Tài khoản không phải admin bị chặn với thông báo rõ", "Đăng nhập test@eshop.com thì hiện lỗi không có quyền, ở lại trang đăng nhập", "FR-12"),
    ("IA-03", "Tất cả", "Bảng dài có phân trang hoặc cuộn với header cố định", "Danh sách nhiều dòng vẫn thấy tiêu đề cột và điều hướng được", "General"),
    ("IA-03", "Quản lý Người dùng", "Checkbox chọn tất cả/chọn dòng có chức năng đi kèm", "Tick checkbox thì có hành động hàng loạt; tick header chọn tất cả dòng", "General"),
    ("IA-03", "Tất cả", "Sau thao tác Sửa, trang cuộn/đưa focus tới form", "Bấm 'Sửa' ở cuối bảng thì người dùng thấy ngay form sửa", "General"),
    # ---------------- IA-04 Feedback / state ----------------
    ("IA-04", "Tất cả", "Hiển thị trạng thái loading khi đang tải dữ liệu", "Bảng/thẻ thống kê có spinner hoặc skeleton khi chờ API", "FR-05"),
    ("IA-04", "Tất cả", "Bảng trống có empty state với icon và thông điệp", "Khi không có dữ liệu hiển thị hình minh họa + thông báo thân thiện", "FR-24"),
    ("IA-04", "Danh mục / Sản phẩm / Coupon / Người dùng", "Thao tác Xóa có hộp thoại xác nhận", "Bấm Xóa hiện hộp thoại xác nhận; chọn Hủy thì dữ liệu giữ nguyên", "FR-24"),
    ("IA-04", "Tất cả", "Thao tác thành công có thông báo phản hồi", "Thêm/sửa/xóa/đổi trạng thái thành công đều có toast xác nhận", "FR-24"),
    ("IA-04", "Tất cả", "Thông báo lỗi bằng tiếng Việt, dễ hiểu, không lộ lỗi kỹ thuật", "Không hiển thị chuỗi như 'Request failed with status code 500'", "FR-21"),
    ("IA-04", "Tất cả", "Thông báo dùng toast/inline thay vì hộp alert() của trình duyệt", "Không xuất hiện hộp thoại alert mặc định của trình duyệt", "General"),
    ("IA-04", "Quản lý Đơn hàng", "Trạng thái đơn được dịch tiếng Việt và phân biệt màu", "5 trạng thái có nhãn tiếng Việt và màu khác nhau", "FR-11, FR-18"),
    ("IA-04", "Quản lý Đơn hàng", "Chỉ hiển thị nút chuyển trạng thái hợp lệ theo state machine", "Đơn 'Đã giao' và 'Đã hủy' không có nút hành động nào", "FR-10, FR-18"),
    ("IA-04", "Quản lý Đơn hàng", "Hủy đơn có hộp thoại xác nhận", "Bấm 'Hủy' hiện xác nhận trước khi đổi trạng thái", "FR-24"),
    ("IA-04", "Quản lý Đơn hàng", "Nút 'Hủy' đơn hàng dùng màu đỏ", "Nút Hủy màu đỏ, phân biệt với nút xác nhận", "FR-21"),
    ("IA-04", "Quản lý Đơn hàng", "Địa chỉ giao hàng hiển thị dạng văn bản an toàn", "Địa chỉ chứa '<b>x</b>' hiển thị nguyên văn, không in đậm/không chạy script", "FR-18, SEC-04"),
    ("IA-04", "Dashboard", "Tổng doanh thu chỉ tính đơn đã giao", "Giá trị bằng tổng tiền các đơn 'Đã giao' trong tab Đơn hàng", "FR-13"),
    ("IA-04", "Dashboard", "Số liệu cập nhật sau khi đổi trạng thái đơn", "Hoàn thành một đơn rồi quay lại Dashboard thì doanh thu tăng đúng", "FR-13"),
    ("IA-04", "Quản lý Sản phẩm", "Sửa một sản phẩm chỉ thay đổi đúng sản phẩm đó", "Sau khi lưu, các dòng khác trong bảng giữ nguyên tên", "FR-15"),
    ("IA-04", "Import CSV", "Nút Import vô hiệu khi chưa có file và báo đang xử lý", "Nút mờ khi chưa chọn file; khi chạy hiển thị 'Đang import...'", "FR-16"),
    ("IA-04", "Import CSV", "Báo cáo kết quả import rõ ràng", "Hiển thị số dòng thành công, số dòng lỗi và lý do từng dòng", "FR-16"),
    ("IA-04", "Import CSV", "Import có dòng lỗi thì rollback toàn bộ và báo rõ", "File có 1 dòng giá âm thì không sản phẩm nào được thêm, thông báo nêu dòng lỗi", "FR-16"),
    ("IA-04", "Quản lý Người dùng", "Không cho xóa tài khoản đang đăng nhập", "Nút Xóa ở dòng admin hiện tại bị ẩn/vô hiệu hoặc có thông báo từ chối", "FR-19"),
    ("IA-04", "Quản lý Người dùng", "Danh sách người dùng không lộ mật khẩu", "Không có cột/giá trị mật khẩu hay hash", "FR-19"),
    ("IA-04", "Quản lý Mã giảm giá", "Coupon hết hạn hiển thị phân biệt nhưng vẫn kèm ngày", "Hiển thị nhãn 'Hết hạn' màu đỏ cùng ngày hết hạn", "FR-17"),
    ("IA-04", "Tất cả", "Phần tử tương tác có trạng thái hover và focus nhìn thấy được", "Nút/menu đổi màu khi hover; có viền focus khi dùng bàn phím", "WCAG 2.1 2.4.7"),
    ("IA-04", "Tất cả", "Nút submit bị khóa khi đang gửi để tránh bấm hai lần", "Bấm nhanh 2 lần 'Thêm mới' chỉ tạo 1 bản ghi", "General"),
    ("IA-04", "Admin Login", "Đăng nhập sai có thông báo rõ nhưng không lộ nguyên nhân", "Hiện 'Email hoặc mật khẩu không đúng' ngay trên form", "FR-02"),
]

HEADERS = ["ID", "Interface Aspect", "Screen", "Checklist item", "Expected result", "Reference",
           "Source", "Why AI missed it", "Status", "Notes", "Screenshot"]
WIDTHS = [9, 10, 22, 45, 55, 14, 18, 30, 10, 40, 25]
IA_NAMES = {"IA-01": "General UI standards", "IA-02": "Forms", "IA-03": "Navigation", "IA-04": "Feedback / state"}

thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
HEAD = dict(font=Font(name="Arial", bold=True, color="FFFFFF"), fill=PatternFill("solid", fgColor="1F4E78"))
BODY = Font(name="Arial", size=10)
WRAP = Alignment(wrap_text=True, vertical="top")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")  # cells the tester fills during execution


def style_header(ws, row=1):
    for c in ws[row]:
        c.font, c.fill, c.border = HEAD["font"], HEAD["fill"], BORDER
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")


def build():
    OUT.mkdir(exist_ok=True)
    rows = [(f"GUI-{i:02d}", *it[:5], SRC, "", "", "", "") for i, it in enumerate(ITEMS, 1)]
    assert len(rows) > 40 and {r[1] for r in rows} == set(IA_NAMES), "need >40 items covering IA-01..04"

    wb = Workbook()
    ws = wb.active
    ws.title = "Checklist"
    ws.append(HEADERS)
    style_header(ws)
    for r in rows:
        ws.append(list(r))
    last = ws.max_row
    for row in ws.iter_rows(min_row=2, max_row=last):
        for c in row:
            c.font, c.alignment, c.border = BODY, WRAP, BORDER
        for c in row[8:11]:
            c.fill = INPUT_FILL
    for i, w in enumerate(WIDTHS):
        ws.column_dimensions[chr(65 + i)].width = w
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = f"A1:K{last}"
    dv = DataValidation(type="list", formula1='"Passed,Failed"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"I2:I{last + 200}")  # room for human-added rows

    s = wb.create_sheet("Summary")
    s.append(["Interface Aspect", "Name", "Designed", "AI items", "Human items", "Executed", "Passed", "Failed"])
    style_header(s)
    rng = lambda col: f"Checklist!${col}$2:${col}${last + 200}"
    for n, (ia, name) in enumerate(IA_NAMES.items(), 2):
        s.append([ia, name,
                  f'=COUNTIF({rng("B")},A{n})',
                  f'=COUNTIFS({rng("B")},A{n},{rng("G")},"AI*")',
                  f'=COUNTIFS({rng("B")},A{n},{rng("G")},"Human")',
                  f'=G{n}+H{n}',
                  f'=COUNTIFS({rng("B")},A{n},{rng("I")},"Passed")',
                  f'=COUNTIFS({rng("B")},A{n},{rng("I")},"Failed")'])
    s.append(["Total", ""] + [f"=SUM({c}2:{c}5)" for c in "CDEFGH"])
    s.append(["Pass rate", "", "", "", "", "", '=IF(F6=0,"",G6/F6)', ""])
    s["G7"].number_format = "0.0%"
    for row in s.iter_rows(min_row=2, max_row=7):
        for c in row:
            c.font, c.border = BODY, BORDER
    for c in s[6] + s[7]:
        c.font = Font(name="Arial", size=10, bold=True)
    for col, w in zip("ABCDEFGH", [16, 22, 11, 10, 12, 10, 10, 10]):
        s.column_dimensions[col].width = w

    g = wb.create_sheet("Legend")
    for line in [
        ["Cách dùng"],
        ["SUT", "EShop Web Admin — http://localhost:5174 (G5: Admin Dashboard + màn hình quản trị)"],
        ["Ô nền vàng", "Điền khi thực thi: Status (chọn Passed/Failed), Notes (lý do Failed), Screenshot (tên file ảnh, chỉ cho Failed)"],
        ["Thêm mục của bạn", "Thêm dòng cuối bảng, ID tiếp theo, Source = Human, điền cột 'Why AI missed it'"],
        ["Ví dụ dòng Human", "GUI-81 | IA-01 | Tất cả | Giao diện dùng được khi zoom 200% | Không mất nội dung/chức năng | WCAG 1.4.4 | Human | Prompt không nêu yêu cầu zoom/accessibility | Failed | Bảng bị cắt cột Hành động | GUI-81_zoom.png"],
        ["Reference", "FR-xx = README đặc tả EShop; General = chuẩn GUI chung (bài giảng GUI checklist); WCAG = Web Content Accessibility Guidelines 2.1"],
    ]:
        g.append(line)
    g["A1"].font = Font(name="Arial", bold=True, size=12)
    for row in g.iter_rows(min_row=2):
        for c in row:
            c.font, c.alignment = BODY, WRAP
    g.column_dimensions["A"].width = 20
    g.column_dimensions["B"].width = 110

    wb.save(OUT / "GUI_Checklist_G5_Admin.xlsx")

    md = ["# GUI Checklist — EShop Web Admin (G5)", "",
          f"Bản AI sinh ban đầu: {len(rows)} mục. Nguồn: {SRC}.", "",
          "| ID | IA | Screen | Checklist item | Expected result | Ref | Source | Why AI missed it | Status | Notes |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    md += ["| " + " | ".join(str(v).replace("|", "\\|") for v in r[:10]) + " |" for r in rows]
    (OUT / "checklist.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(rows)} items -> {OUT}")


if __name__ == "__main__":
    build()
