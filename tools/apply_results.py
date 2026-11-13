"""Write Task 1 execution results (Status / Notes / Screenshot) into the checklist workbook + Markdown.

Environment of this run: Chromium (Claude desktop in-app browser), Windows 11, viewport 1024x768,
EShop Web Admin http://localhost:5174, fresh seed data + tools' sample orders. Executed 2026-11-13.
Usage: python tools/apply_results.py
"""
from pathlib import Path
from openpyxl import load_workbook

DIR = Path(__file__).resolve().parent.parent / "task1-gui-checklist"
P, F = "Passed", "Failed"

# id: (status, notes, screenshot)
RESULTS = {
    1: (F, "Còn tiếng Anh: 'Admin Login', 'Password', 'Login', '(Delivered)', cột 'Role', nút trình duyệt 'Choose File'.", "login_screen.jpg"),
    2: (F, "Tiêu đề 'Admin Login', placeholder 'Password', nút 'Login' đều tiếng Anh.", "login_screen.jpg"),
    3: (F, "Thẻ <h1> duy nhất là logo 'EShop Admin' ở mọi màn hình; tiêu đề màn hình dùng <h2>. Trang đăng nhập không có <h1>.", "login_screen.jpg"),
    4: (F, "'Lưu sản phẩm' màu xanh lá, 'Tạo mã' màu cam, 'Xác nhận' (đơn) màu tím; chỉ 'Thêm mới', 'Import' là xanh dương.", "csv_no_rollback.jpg"),
    5: (F, "Nút 'Hủy' đơn hàng màu xám (rgb 156,163,175), không phải đỏ.", "orders_xss_and_invalid_actions.jpg"),
    6: (F, "Không thống nhất: bảng sản phẩm '30000000 ₫' (không phân cách); đơn hàng/coupon/dashboard dùng dấu phẩy '28,000,000 ₫' thay vì dấu chấm kiểu VN.", "products_edit_renames_all.jpg"),
    7: (F, "Cột Giá hiển thị '30000000 ₫', '-1000 ₫', ' ₫' (giá rỗng).", "products_edit_renames_all.jpg"),
    8: (F, "Nhãn 'Tổng doanh thu (Delivered)' trộn tiếng Anh.", "dashboard_revenue_x2.jpg"),
    9: (P, "", ""),
    10: (F, "Cách viết hoa menu không thống nhất: 'Mã Giảm Giá' (hoa mọi chữ) so với 'Danh mục', 'Sản phẩm'.", "orders_xss_and_invalid_actions.jpg"),
    11: (F, "'Tên Danh Mục' (hoa mọi chữ) vs 'Tên SP', 'Giới hạn/người', 'Hành động'.", "categories_blank_and_duplicate.jpg"),
    12: (F, "Dùng viết tắt/tiếng Anh: 'Tên SP', 'Số ĐT', 'Role'.", "users_admin_deleted_self.jpg"),
    13: (F, "Nhấn Tab từ đầu trang bỏ qua toàn bộ sidebar (các <li> không focus được); focus đi thẳng vào ô nhập nội dung.", "categories_tab-order.jpg"),
    14: (P, "alt = tên sản phẩm. Ghi chú: sản phẩm không có URL ảnh hiển thị icon ảnh hỏng + alt text.", ""),
    15: (P, "", ""),
    16: (F, "Chữ trắng trên nút: 'Sửa' vàng 1.92:1, 'Đánh dấu Đã giao'/'Hoàn thành' 2.28:1, 'Hủy' xám 2.54:1, 'Tạo mã' cam 2.8:1, 'Lưu sản phẩm' 3.3:1, 'Xóa' 3.76:1; số doanh thu xanh lá 3.3:1 (< 4.5:1).", "products_edit_renames_all.jpg"),
    17: (P, "Không cuộn ngang ở 1024px với dữ liệu mẫu. Ghi chú: tên sản phẩm 300 ký tự không xuống dòng làm bảng rộng 3163px.", ""),
    18: (P, "", ""),
    19: (F, "Trường Email là type=\"text\"; nhập 'abc' vẫn submit được (không có validate HTML5).", "login_screen.jpg"),
    20: (P, "", ""),
    21: (F, "Không có <label> nào trên mọi form; chỉ dùng placeholder, nhãn biến mất khi đã nhập.", "csv_no_rollback.jpg"),
    22: (F, "Không có dấu * ở bất kỳ trường bắt buộc nào.", "csv_no_rollback.jpg"),
    23: (F, "Bấm 'Thêm mới' khi để trống tạo danh mục tên rỗng (#4), không có thông báo lỗi.", "categories_blank_and_duplicate.jpg"),
    24: (F, "Nhập '   ' tạo danh mục tên rỗng (#5).", "categories_blank_and_duplicate.jpg"),
    25: (P, "Bị chặn bởi thuộc tính required; thông báo là của trình duyệt ('Please fill out this field.').", ""),
    26: (F, "Nhập và lưu được tên 300 ký tự, không có maxlength hay thông báo lỗi.", "products_edit_renames_all.jpg"),
    27: (F, "Để trống Giá vẫn lưu được sản phẩm (giá hiển thị ' ₫').", "products_edit_renames_all.jpg"),
    28: (F, "Lưu được giá 0 và -1000.", "products_edit_renames_all.jpg"),
    29: (F, "Dropdown luôn mặc định 'Điện thoại', không có lựa chọn 'Chọn danh mục'; người dùng có thể vô tình lưu sai danh mục.", "csv_no_rollback.jpg"),
    30: (P, "", ""),
    31: (P, "", ""),
    32: (F, "Input file không có accept=.csv; chọn 'data.txt' vẫn hiện 'Import 1 sản phẩm'.", "csv_quoted_comma_split.jpg"),
    33: (P, "", ""),
    34: (F, "Dòng '\"QA Ao, quan\",150000,\"Mo ta, co dau phay\"' bị tách thành 5 ô sai: name='\"QA Ao', price='quan\"', description='150000'...", "csv_quoted_comma_split.jpg"),
    35: (P, "", ""),
    36: (F, "Tạo được coupon QAZERO giá trị 0%.", "coupons_invalid_values.jpg"),
    37: (F, "Tạo được coupon QA150 giảm 150%.", "coupons_invalid_values.jpg"),
    38: (F, "Tạo được coupon QAMINNEG đơn tối thiểu -5 ₫.", "coupons_invalid_values.jpg"),
    39: (P, "Trình duyệt chặn 0 nhờ min=1.", ""),
    40: (F, "Tạo được coupon QAPAST hết hạn 2020-01-01; date picker không có min.", "coupons_invalid_values.jpg"),
    41: (F, "Mã trùng bị từ chối nhưng thông báo là lỗi kỹ thuật: 'Lỗi: SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code' (qua alert).", "coupons_invalid_values.jpg"),
    42: (F, "Không có thông báo lỗi inline nào trên các form; lỗi chỉ hiện qua alert() hoặc không hiện.", "csv_no_rollback.jpg"),
    43: (P, "", ""),
    44: (P, "", ""),
    45: (P, "Mục đang chọn đổi màu xanh (text-blue-400).", ""),
    46: (F, "Mục menu là <li onClick>, tabIndex=-1, không có role; không thể dùng Tab/Enter.", "categories_tab-order.jpg"),
    47: (P, "", ""),
    48: (P, "Sau đăng xuất lịch sử trình duyệt chỉ có 1 mục, Back không quay lại dữ liệu admin.", ""),
    49: (F, "Mọi màn hình đều ở URL 'http://localhost:5174/' (chuyển tab bằng state); không thể copy/bookmark một màn hình.", "dashboard_revenue_x2.jpg"),
    50: (F, "F5 khi đang ở 'Đơn hàng' bị đưa về 'Dashboard'.", "dashboard_revenue_x2.jpg"),
    51: (F, "Chuyển tab không tạo lịch sử (history.length=1); Back rời khỏi ứng dụng thay vì về màn hình trước.", "dashboard_revenue_x2.jpg"),
    52: (F, "Không có breadcrumb ở bất kỳ màn hình nào.", "orders_xss_and_invalid_actions.jpg"),
    53: (P, "Đăng nhập test@eshop.com: 'Bạn không phải là admin!' và ở lại trang đăng nhập (thông báo qua alert, xem GUI-62).", ""),
    54: (F, "Bảng 30 sản phẩm không phân trang; thead position=static nên tiêu đề cột cuộn mất.", "products_long_table_no_pagination.jpg"),
    55: (F, "Tick checkbox header không chọn các dòng; không có hành động hàng loạt nào.", "users_admin_deleted_self.jpg"),
    56: (F, "Bấm 'Sửa' ở dòng cuối bảng: form sửa nằm ngoài màn hình (top = -356px), không tự cuộn/focus.", "products_edit_renames_all.jpg"),
    57: (F, "Không có spinner/skeleton; khi backend không phản hồi màn hình chỉ hiện bảng trống, không báo lỗi.", "backend_down_no_loading_empty_state.jpg"),
    58: (F, "Bảng không có dữ liệu chỉ hiện dòng tiêu đề, không icon, không thông điệp.", "backend_down_no_loading_empty_state.jpg"),
    59: (F, "Bấm 'Xóa' (danh mục, sản phẩm, coupon, người dùng) xóa ngay, không có hộp xác nhận.", "users_admin_deleted_self.jpg"),
    60: (F, "Thêm danh mục/sản phẩm/coupon, xóa, đổi trạng thái đơn đều không có phản hồi thành công; chỉ 'Sửa sản phẩm' có alert 'Cập nhật thành công!'.", "categories_blank_and_duplicate.jpg"),
    61: (F, "Hiển thị lỗi kỹ thuật cho người dùng: 'SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code'; các lỗi khác ghép err.message (VD 'Request failed with status code ...').", "coupons_invalid_values.jpg"),
    62: (F, "Mọi thông báo dùng alert() của trình duyệt: 'Đăng nhập thất bại', 'Bạn không phải là admin!', 'Cập nhật thành công!', 'Lỗi: ...'. (alert không xuất hiện trong ảnh chụp trang.)", "login_screen.jpg"),
    63: (P, "", ""),
    64: (F, "Đơn 'Đã hủy' (#6) vẫn có nút 'Đánh dấu Đã giao' — vi phạm trạng thái kết thúc của FR-10.", "orders_xss_and_invalid_actions.jpg"),
    65: (F, "Bấm 'Hủy' đơn #7 đổi trạng thái ngay, không xác nhận.", "orders_xss_and_invalid_actions.jpg"),
    66: (F, "Nút 'Hủy' màu xám.", "orders_xss_and_invalid_actions.jpg"),
    67: (F, "Địa chỉ '<b>…</b><img src=x onerror=…>' được render HTML: chữ in đậm, ảnh hỏng chèn vào và onerror chạy (XSS).", "orders_xss_and_invalid_actions.jpg"),
    68: (F, "Chỉ đơn #5 (135.000.000 ₫) đã giao nhưng hiển thị 270,000,000 ₫; sau khi giao thêm đơn #4 (64tr) hiển thị 398,000,000 ₫ (gấp đôi).", "dashboard_revenue_x2.jpg"),
    69: (P, "Số liệu có cập nhật khi đổi tab (giá trị sai thuộc GUI-68). Ghi chú: đơn mới đặt từ web không hiện cho tới khi tải lại trang.", ""),
    70: (F, "Sửa tên 1 sản phẩm thành 'QA SP da sua' thì cả 9 dòng trong bảng đổi tên; DB chỉ đổi đúng 1 (tải lại thì đúng).", "products_edit_renames_all.jpg"),
    71: (P, "Nút disabled + 'Import 0 sản phẩm' khi chưa chọn file. Nhãn 'Đang import...' có trong UI nhưng quá nhanh để quan sát.", ""),
    72: (F, "File có 1 dòng giá -5 vẫn báo '✅ Import hoàn tất: 2/2'; không có số dòng lỗi/lý do.", "csv_no_rollback.jpg"),
    73: (F, "Không rollback: dòng giá -5 được import cùng dòng hợp lệ (2 sản phẩm thêm vào).", "csv_no_rollback.jpg"),
    74: (F, "Admin bấm Xóa ở dòng chính mình: tài khoản admin@eshop.com bị xóa ngay, không xác nhận, không chặn.", "users_admin_deleted_self.jpg"),
    75: (P, "UI không hiển thị mật khẩu. Ghi chú: API trả thêm login_attempts, locked_until.", ""),
    76: (F, "Coupon hết hạn chỉ hiện chữ 'Hết hạn', ẩn mất ngày hết hạn.", "coupons_invalid_values.jpg"),
    77: (F, "Nút không đổi màu khi hover (rgb 37,99,235 trước/sau); mục sidebar không nhận focus nên không có viền focus.", "products_edit_renames_all.jpg"),
    78: (F, "Bấm 'Thêm mới' 2 lần liên tiếp tạo 2 danh mục 'QA Test DM' (#6, #7); nút không bị khóa.", "categories_blank_and_duplicate.jpg"),
    79: (F, "Chỉ hiện alert 'Đăng nhập thất bại', không có thông báo trên form. Thêm: sau 2 lần sai tài khoản bị khóa 3 phút (FR-02: khóa 30 giây sau 3 lần).", "login_screen.jpg"),
}


def main():
    path = DIR / "GUI_Checklist_G5_Admin.xlsx"
    wb = load_workbook(path)
    ws = wb["Checklist"]
    by_id = {ws.cell(r, 1).value: r for r in range(2, ws.max_row + 1)}
    for n, (status, notes, shot) in RESULTS.items():
        r = by_id[f"GUI-{n:02d}"]
        ws.cell(r, 9).value, ws.cell(r, 10).value = status, notes or None
        ws.cell(r, 11).value = f"screenshots/{shot}" if shot else None
        assert status == P or shot, f"Failed item GUI-{n:02d} needs a screenshot"
    wb.save(path)

    # regenerate Markdown from the workbook so both stay identical
    rows = [[c.value or "" for c in row[:11]] for row in ws.iter_rows(min_row=2)]
    passed = sum(r[8] == P for r in rows)
    failed = sum(r[8] == F for r in rows)
    md = ["# GUI Checklist — EShop Web Admin (G5)", "",
          f"Thiết kế: {len(rows)} mục · Thực thi: {passed + failed} · Passed: {passed} · Failed: {failed}", "",
          "Môi trường: Chromium (trình duyệt trong Claude desktop), Windows 11, 1024×768, http://localhost:5174, ngày 2026-11-13.", "",
          "| ID | IA | Screen | Checklist item | Expected result | Ref | Source | Why AI missed it | Status | Notes | Screenshot |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    md += ["| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in r) + " |" for r in rows]
    (DIR / "checklist.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"executed {passed + failed}/{len(rows)}: {passed} passed, {failed} failed")


if __name__ == "__main__":
    main()
