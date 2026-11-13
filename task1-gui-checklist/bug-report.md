# Bug Report — EShop Web Admin (G5)

**Môi trường:** Windows 11 · Chromium (trình duyệt trong Claude desktop) · viewport 1024×768 · Web Admin `http://localhost:5174` · Backend `http://localhost:3000` · tài khoản `admin@eshop.com` · ngày 2026-11-13.
**Nguồn:** thực thi GUI checklist ([checklist.md](checklist.md)). Mỗi bug gom các mục Failed có cùng nguyên nhân.

Mức độ (Severity): **Critical** = mất dữ liệu/bảo mật · **High** = sai nghiệp vụ hoặc chặn thao tác chính · **Medium** = sai đặc tả, có cách vượt qua · **Low** = thẩm mỹ, nhất quán.

| Bug | Tiêu đề | Severity | Checklist |
|---|---|---|---|
| BUG-01 | Địa chỉ giao hàng render HTML, chạy được script (XSS) | Critical | GUI-67 |
| BUG-02 | Admin xóa được chính tài khoản đang đăng nhập | Critical | GUI-74 |
| BUG-03 | Mọi thao tác Xóa / Hủy đơn không có hộp xác nhận | High | GUI-59, GUI-65 |
| BUG-04 | Doanh thu Dashboard bị nhân đôi | High | GUI-68 |
| BUG-05 | Đơn đã hủy vẫn có nút "Đánh dấu Đã giao" | High | GUI-64 |
| BUG-06 | Sửa 1 sản phẩm làm bảng hiển thị đổi tên tất cả sản phẩm | High | GUI-70 |
| BUG-07 | Import CSV không rollback khi có dòng lỗi, báo cáo không nêu lỗi | High | GUI-72, GUI-73 |
| BUG-08 | Form sản phẩm nhận giá rỗng, 0, âm và tên > 255 ký tự | High | GUI-26, GUI-27, GUI-28 |
| BUG-09 | Thêm được danh mục tên rỗng / toàn khoảng trắng | Medium | GUI-23, GUI-24 |
| BUG-10 | Form coupon nhận giá trị 0, 150%, đơn tối thiểu âm, ngày quá khứ | Medium | GUI-36, GUI-37, GUI-38, GUI-40 |
| BUG-11 | Import CSV tách sai trường có dấu phẩy trong nháy kép | Medium | GUI-34 |
| BUG-12 | Ô chọn file import nhận file không phải .csv | Medium | GUI-32 |
| BUG-13 | Bấm nút submit 2 lần tạo bản ghi trùng | Medium | GUI-78 |
| BUG-14 | Thông báo lỗi lộ chi tiết kỹ thuật (SQLITE_CONSTRAINT) | Medium | GUI-41, GUI-61 |
| BUG-15 | Phản hồi dùng alert() trình duyệt, không có thông báo inline/toast, thiếu thông báo thành công | Medium | GUI-42, GUI-60, GUI-62, GUI-79 |
| BUG-16 | Không có trạng thái loading, lỗi tải dữ liệu và empty state | Medium | GUI-57, GUI-58 |
| BUG-17 | Menu sidebar không dùng được bằng bàn phím | Medium | GUI-13, GUI-46, GUI-77 |
| BUG-18 | Màn hình không có URL riêng; F5 và nút Back hoạt động sai | Medium | GUI-49, GUI-50, GUI-51 |
| BUG-19 | Ô nhập không có nhãn và dấu * cho trường bắt buộc | Medium | GUI-21, GUI-22 |
| BUG-20 | Trường Email đăng nhập dùng type="text" | Low | GUI-19 |
| BUG-21 | Độ tương phản chữ trên nút thấp hơn WCAG AA | Medium | GUI-16 |
| BUG-22 | Màu nút không theo quy ước (tích cực = xanh dương, nguy hiểm = đỏ) | Low | GUI-04, GUI-05, GUI-66 |
| BUG-23 | Định dạng tiền tệ không thống nhất, giá sản phẩm không phân cách hàng nghìn | Low | GUI-06, GUI-07 |
| BUG-24 | Giao diện còn tiếng Anh, viết tắt và viết hoa không thống nhất | Low | GUI-01, GUI-02, GUI-08, GUI-10, GUI-11, GUI-12 |
| BUG-25 | Không có thẻ h1 cho tiêu đề màn hình | Low | GUI-03 |
| BUG-26 | Không có breadcrumb | Low | GUI-52 |
| BUG-27 | Bảng dài không phân trang, tiêu đề cột không cố định | Low | GUI-54 |
| BUG-28 | Checkbox chọn tất cả ở bảng Người dùng không hoạt động | Low | GUI-55 |
| BUG-29 | Bấm "Sửa" ở cuối bảng không đưa người dùng tới form sửa | Low | GUI-56 |
| BUG-30 | Dropdown danh mục không có lựa chọn mặc định "Chọn danh mục" | Low | GUI-29 |
| BUG-31 | Coupon hết hạn bị ẩn ngày hết hạn | Low | GUI-76 |
| BUG-32 | Đăng nhập sai 2 lần đã khóa tài khoản 3 phút (đặc tả: 3 lần, 30 giây) | Medium | GUI-79 |

---

## BUG-01 — Địa chỉ giao hàng render HTML, chạy được script (XSS)
- **Severity:** Critical · **Màn hình:** Quản lý Đơn hàng · **Đặc tả:** FR-18, SEC-04
- **Bước tái hiện:**
  1. Đăng nhập web với `test@eshop.com`, đặt hàng với địa chỉ `<b>QA dia chi in dam</b><img src=x onerror="window.__xss=1">`.
  2. Đăng nhập admin, mở **Đơn hàng**.
- **Mong đợi:** địa chỉ hiển thị nguyên văn dạng text.
- **Thực tế:** chữ được in đậm, thẻ `<img>` được chèn vào và `onerror` chạy (`window.__xss === 1`). Kẻ tấn công có thể chạy JavaScript trong phiên admin.
- **Ảnh:** [orders_xss_and_invalid_actions.jpg](screenshots/orders_xss_and_invalid_actions.jpg)

## BUG-02 — Admin xóa được chính tài khoản đang đăng nhập
- **Severity:** Critical · **Màn hình:** Quản lý Người dùng · **Đặc tả:** FR-19
- **Bước tái hiện:** Đăng nhập `admin@eshop.com` → **Người dùng** → bấm **Xóa** ở dòng `admin@eshop.com`.
- **Mong đợi:** nút bị ẩn/vô hiệu hoặc hệ thống từ chối.
- **Thực tế:** tài khoản admin bị xóa ngay, không hỏi xác nhận; không còn tài khoản quản trị nào.
- **Ảnh:** [users_admin_deleted_self.jpg](screenshots/users_admin_deleted_self.jpg)

## BUG-03 — Mọi thao tác Xóa / Hủy đơn không có hộp xác nhận
- **Severity:** High · **Màn hình:** Danh mục, Sản phẩm, Mã giảm giá, Người dùng, Đơn hàng · **Đặc tả:** FR-24
- **Bước tái hiện:** Bấm **Xóa** ở bất kỳ dòng nào (hoặc **Hủy** ở một đơn chờ xác nhận).
- **Mong đợi:** hộp thoại xác nhận, chọn Hủy thì dữ liệu giữ nguyên.
- **Thực tế:** dữ liệu bị xóa / đơn bị hủy ngay lập tức.
- **Ảnh:** [users_admin_deleted_self.jpg](screenshots/users_admin_deleted_self.jpg), [orders_xss_and_invalid_actions.jpg](screenshots/orders_xss_and_invalid_actions.jpg)

## BUG-04 — Doanh thu Dashboard bị nhân đôi
- **Severity:** High · **Màn hình:** Dashboard · **Đặc tả:** FR-13
- **Bước tái hiện:** Có đúng 1 đơn **Đã giao** trị giá 135.000.000 ₫ → mở **Dashboard**. Sau đó bấm **Hoàn thành** đơn đang giao 64.000.000 ₫ → quay lại Dashboard.
- **Mong đợi:** 135.000.000 ₫, sau đó 199.000.000 ₫.
- **Thực tế:** 270,000,000 ₫, sau đó 398,000,000 ₫ (gấp đôi).
- **Ảnh:** [dashboard_revenue_x2.jpg](screenshots/dashboard_revenue_x2.jpg)

## BUG-05 — Đơn đã hủy vẫn có nút "Đánh dấu Đã giao"
- **Severity:** High · **Màn hình:** Quản lý Đơn hàng · **Đặc tả:** FR-10, FR-18
- **Bước tái hiện:** Mở **Đơn hàng**, xem một đơn trạng thái **Đã hủy**.
- **Mong đợi:** không có nút hành động (trạng thái kết thúc).
- **Thực tế:** có nút **Đánh dấu Đã giao**; bấm vào chuyển đơn đã hủy thành đã giao.
- **Ảnh:** [orders_xss_and_invalid_actions.jpg](screenshots/orders_xss_and_invalid_actions.jpg)

## BUG-06 — Sửa 1 sản phẩm làm bảng hiển thị đổi tên tất cả sản phẩm
- **Severity:** High · **Màn hình:** Quản lý Sản phẩm · **Đặc tả:** FR-15
- **Bước tái hiện:** Bấm **Sửa** ở một sản phẩm → đổi tên thành `QA SP da sua` → **Lưu sản phẩm**.
- **Mong đợi:** chỉ dòng đó đổi tên.
- **Thực tế:** cả 9 dòng hiển thị tên `QA SP da sua` (database chỉ đổi đúng 1; F5 thì hiển thị đúng lại). Admin có thể tưởng dữ liệu bị hỏng.
- **Ảnh:** [products_edit_renames_all.jpg](screenshots/products_edit_renames_all.jpg)

## BUG-07 — Import CSV không rollback khi có dòng lỗi, báo cáo không nêu lỗi
- **Severity:** High · **Màn hình:** Quản lý Sản phẩm → Import CSV · **Đặc tả:** FR-16
- **Bước tái hiện:** Import file:
  ```
  name,price,description,imageUrl,category_id
  QA Good Row,100000,ok,,1
  QA Bad Row,-5,bad,,1
  ```
- **Mong đợi:** không dòng nào được thêm; báo cáo "1 dòng lỗi: dòng 3 giá phải > 0".
- **Thực tế:** "✅ Import hoàn tất: 2/2 sản phẩm được thêm" — sản phẩm giá -5 được lưu.
- **Ảnh:** [csv_no_rollback.jpg](screenshots/csv_no_rollback.jpg)

## BUG-08 — Form sản phẩm nhận giá rỗng, 0, âm và tên > 255 ký tự
- **Severity:** High · **Màn hình:** Quản lý Sản phẩm · **Đặc tả:** FR-15
- **Bước tái hiện:** Nhập tên bất kỳ và lần lượt giá: để trống, `0`, `-1000`; nhập tên 300 ký tự với giá 1000 → **Lưu sản phẩm**.
- **Mong đợi:** bị chặn với thông báo lỗi.
- **Thực tế:** cả 4 sản phẩm đều được lưu; bảng hiện `₫`, `0 ₫`, `-1000 ₫`.
- **Ảnh:** [products_edit_renames_all.jpg](screenshots/products_edit_renames_all.jpg)

## BUG-09 — Thêm được danh mục tên rỗng / toàn khoảng trắng
- **Severity:** Medium · **Màn hình:** Quản lý Danh mục · **Đặc tả:** FR-14
- **Bước tái hiện:** Để trống ô (hoặc nhập `   `) → **Thêm mới**.
- **Mong đợi:** thông báo "Tên danh mục là bắt buộc".
- **Thực tế:** tạo danh mục không tên (#4, #5), không có thông báo.
- **Ảnh:** [categories_blank_and_duplicate.jpg](screenshots/categories_blank_and_duplicate.jpg)

## BUG-10 — Form coupon nhận giá trị 0, 150%, đơn tối thiểu âm, ngày quá khứ
- **Severity:** Medium · **Màn hình:** Quản lý Mã giảm giá · **Đặc tả:** FR-17
- **Bước tái hiện:** Tạo lần lượt `QAZERO` (giá trị 0), `QA150` (150%), `QAMINNEG` (đơn tối thiểu -5), `QAPAST` (hết hạn 2020-01-01).
- **Mong đợi:** bị chặn với thông báo lỗi.
- **Thực tế:** cả 4 mã được tạo.
- **Ảnh:** [coupons_invalid_values.jpg](screenshots/coupons_invalid_values.jpg)

## BUG-11 — Import CSV tách sai trường có dấu phẩy trong nháy kép
- **Severity:** Medium · **Màn hình:** Import CSV · **Đặc tả:** FR-16 (RFC 4180)
- **Bước tái hiện:** Chọn file có dòng `"QA Ao, quan",150000,"Mo ta, co dau phay",,1`.
- **Mong đợi:** xem trước name = `QA Ao, quan`, price = `150000`.
- **Thực tế:** name = `"QA Ao`, price = `quan"`, description = `150000`… (lệch cột).
- **Ảnh:** [csv_quoted_comma_split.jpg](screenshots/csv_quoted_comma_split.jpg)

## BUG-12 — Ô chọn file import nhận file không phải .csv
- **Severity:** Medium · **Màn hình:** Import CSV · **Đặc tả:** FR-16
- **Bước tái hiện:** Chọn file `data.txt`.
- **Mong đợi:** hộp chọn chỉ hiện file .csv; file sai đuôi bị báo lỗi.
- **Thực tế:** file được nhận, nút hiện "Import 1 sản phẩm".
- **Ảnh:** [csv_quoted_comma_split.jpg](screenshots/csv_quoted_comma_split.jpg)

## BUG-13 — Bấm nút submit 2 lần tạo bản ghi trùng
- **Severity:** Medium · **Màn hình:** Quản lý Danh mục (tương tự các form khác)
- **Bước tái hiện:** Nhập `QA Test DM` → bấm **Thêm mới** 2 lần liên tiếp.
- **Mong đợi:** 1 bản ghi; nút khóa trong lúc gửi.
- **Thực tế:** 2 danh mục `QA Test DM` (#6, #7).
- **Ảnh:** [categories_blank_and_duplicate.jpg](screenshots/categories_blank_and_duplicate.jpg)

## BUG-14 — Thông báo lỗi lộ chi tiết kỹ thuật
- **Severity:** Medium · **Màn hình:** Quản lý Mã giảm giá (và các form khác) · **Đặc tả:** FR-21
- **Bước tái hiện:** Tạo coupon với mã `SAVE10` (đã tồn tại).
- **Mong đợi:** "Mã giảm giá đã tồn tại".
- **Thực tế:** alert `Lỗi: SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code`.
- **Ảnh:** [coupons_invalid_values.jpg](screenshots/coupons_invalid_values.jpg)

## BUG-15 — Phản hồi dùng alert() trình duyệt, không có thông báo inline/toast
- **Severity:** Medium · **Màn hình:** Tất cả · **Đặc tả:** FR-22, FR-24
- **Bước tái hiện:** Đăng nhập sai mật khẩu; thêm danh mục; sửa sản phẩm.
- **Mong đợi:** lỗi hiện inline phía trên nút submit; thao tác thành công có toast.
- **Thực tế:** lỗi hiện bằng hộp `alert()` ("Đăng nhập thất bại"); thêm/xóa thành công không có phản hồi; chỉ sửa sản phẩm có alert "Cập nhật thành công!".
- **Ảnh:** [login_screen.jpg](screenshots/login_screen.jpg)

## BUG-16 — Không có trạng thái loading, lỗi tải dữ liệu và empty state
- **Severity:** Medium · **Màn hình:** Tất cả · **Đặc tả:** FR-05, FR-24
- **Bước tái hiện:** Tắt backend → tải lại Web Admin → mở **Danh mục**.
- **Mong đợi:** loading khi chờ; thông báo lỗi kết nối; bảng trống có icon + thông điệp.
- **Thực tế:** chỉ có dòng tiêu đề bảng, không loading, không báo lỗi.
- **Ảnh:** [backend_down_no_loading_empty_state.jpg](screenshots/backend_down_no_loading_empty_state.jpg)

## BUG-17 — Menu sidebar không dùng được bằng bàn phím
- **Severity:** Medium · **Màn hình:** Sidebar · **Đặc tả:** FR-21 (Tab order), WCAG 2.1.1
- **Bước tái hiện:** Đặt focus đầu trang, nhấn Tab nhiều lần.
- **Mong đợi:** focus đi qua từng mục menu, Enter mở màn hình, có viền focus.
- **Thực tế:** focus bỏ qua toàn bộ menu (phần tử `<li>` không focus được); nút không có trạng thái hover.
- **Ảnh:** [categories_tab-order.jpg](screenshots/categories_tab-order.jpg)

## BUG-18 — Màn hình không có URL riêng; F5 và nút Back hoạt động sai
- **Severity:** Medium · **Màn hình:** Tất cả
- **Bước tái hiện:** Mở **Đơn hàng** → nhấn F5; hoặc chuyển Sản phẩm → Đơn hàng rồi nhấn Back.
- **Mong đợi:** F5 giữ màn hình Đơn hàng; Back về Sản phẩm; mỗi màn hình có URL.
- **Thực tế:** URL luôn là `/`; F5 về Dashboard; Back rời khỏi ứng dụng.
- **Ảnh:** [dashboard_revenue_x2.jpg](screenshots/dashboard_revenue_x2.jpg) (trang sau F5 ở Đơn hàng)

## BUG-19 — Ô nhập không có nhãn và dấu * cho trường bắt buộc
- **Severity:** Medium · **Màn hình:** Tất cả form · **Đặc tả:** FR-22
- **Thực tế:** không có `<label>` nào; chỉ placeholder (mất khi đã nhập); không có dấu `*`.
- **Ảnh:** [csv_no_rollback.jpg](screenshots/csv_no_rollback.jpg)

## BUG-20 — Trường Email đăng nhập dùng type="text"
- **Severity:** Low · **Màn hình:** Admin Login · **Đặc tả:** FR-22
- **Bước tái hiện:** Nhập `abc` vào Email → Login.
- **Mong đợi:** trình duyệt báo định dạng email sai.
- **Thực tế:** form gửi lên server; `type="text"`.
- **Ảnh:** [login_screen.jpg](screenshots/login_screen.jpg)

## BUG-21 — Độ tương phản chữ trên nút thấp hơn WCAG AA
- **Severity:** Medium · **Màn hình:** Sản phẩm, Đơn hàng, Mã giảm giá, Dashboard · **Chuẩn:** WCAG 2.1 1.4.3 (≥ 4.5:1)
- **Thực tế (đo bằng computed style):** "Sửa" 1.92:1, "Hoàn thành"/"Đánh dấu Đã giao" 2.28:1, "Hủy" 2.54:1, "Tạo mã" 2.8:1, "Lưu sản phẩm" 3.3:1, "Xóa" 3.76:1, số doanh thu 3.3:1.
- **Ảnh:** [products_edit_renames_all.jpg](screenshots/products_edit_renames_all.jpg)

## BUG-22 — Màu nút không theo quy ước
- **Severity:** Low · **Đặc tả:** FR-21
- **Thực tế:** "Lưu sản phẩm" xanh lá, "Tạo mã" cam, "Xác nhận" tím; "Hủy" đơn hàng xám thay vì đỏ.
- **Ảnh:** [csv_no_rollback.jpg](screenshots/csv_no_rollback.jpg), [orders_xss_and_invalid_actions.jpg](screenshots/orders_xss_and_invalid_actions.jpg)

## BUG-23 — Định dạng tiền tệ không thống nhất
- **Severity:** Low · **Đặc tả:** FR-21
- **Thực tế:** bảng sản phẩm `30000000 ₫` (không phân cách); đơn hàng/coupon/dashboard `28,000,000 ₫` (dấu phẩy kiểu Mỹ).
- **Ảnh:** [products_edit_renames_all.jpg](screenshots/products_edit_renames_all.jpg)

## BUG-24 — Giao diện còn tiếng Anh, viết tắt, viết hoa không thống nhất
- **Severity:** Low · **Đặc tả:** FR-21
- **Thực tế:** "Admin Login", "Password", "Login", "(Delivered)", "Role"; viết tắt "Tên SP", "Số ĐT"; "Tên Danh Mục"/"Mã Giảm Giá" hoa mọi chữ, các nhãn khác viết thường.
- **Ảnh:** [login_screen.jpg](screenshots/login_screen.jpg), [users_admin_deleted_self.jpg](screenshots/users_admin_deleted_self.jpg)

## BUG-25 — Không có thẻ h1 cho tiêu đề màn hình
- **Severity:** Low · **Đặc tả:** FR-21
- **Thực tế:** `<h1>` duy nhất là logo "EShop Admin"; tiêu đề màn hình là `<h2>`; trang đăng nhập không có `<h1>`.
- **Ảnh:** [login_screen.jpg](screenshots/login_screen.jpg)

## BUG-26 — Không có breadcrumb
- **Severity:** Low · **Đặc tả:** FR-23 · **Ảnh:** [orders_xss_and_invalid_actions.jpg](screenshots/orders_xss_and_invalid_actions.jpg)

## BUG-27 — Bảng dài không phân trang, tiêu đề cột không cố định
- **Severity:** Low · **Bước tái hiện:** import 25 sản phẩm → cuộn bảng Sản phẩm (30 dòng).
- **Thực tế:** không phân trang; tiêu đề cột cuộn mất. · **Ảnh:** [products_long_table_no_pagination.jpg](screenshots/products_long_table_no_pagination.jpg)

## BUG-28 — Checkbox chọn tất cả ở bảng Người dùng không hoạt động
- **Severity:** Low · **Thực tế:** tick checkbox tiêu đề không chọn dòng nào; không có hành động hàng loạt. · **Ảnh:** [users_admin_deleted_self.jpg](screenshots/users_admin_deleted_self.jpg)

## BUG-29 — Bấm "Sửa" ở cuối bảng không đưa người dùng tới form sửa
- **Severity:** Low · **Thực tế:** form nằm phía trên ngoài màn hình (top = -356px); người dùng không thấy đã vào chế độ sửa. · **Ảnh:** [products_edit_renames_all.jpg](screenshots/products_edit_renames_all.jpg)

## BUG-30 — Dropdown danh mục không có lựa chọn mặc định
- **Severity:** Low · **Đặc tả:** FR-15 · **Thực tế:** luôn chọn sẵn "Điện thoại", dễ lưu nhầm danh mục. · **Ảnh:** [csv_no_rollback.jpg](screenshots/csv_no_rollback.jpg)

## BUG-31 — Coupon hết hạn bị ẩn ngày hết hạn
- **Severity:** Low · **Thực tế:** cột Hết hạn chỉ hiện chữ "Hết hạn" màu đỏ, không còn ngày. · **Ảnh:** [coupons_invalid_values.jpg](screenshots/coupons_invalid_values.jpg)

## BUG-32 — Đăng nhập sai 2 lần đã khóa tài khoản 3 phút
- **Severity:** Medium · **Màn hình:** Admin Login · **Đặc tả:** FR-02 (khóa 30 giây sau 3 lần sai, bộ đếm tăng 1)
- **Bước tái hiện:** Nhập sai mật khẩu admin 2 lần → nhập đúng mật khẩu.
- **Mong đợi:** đăng nhập thành công (mới sai 2 lần).
- **Thực tế:** "Đăng nhập thất bại"; API trả `403 Tài khoản đã bị khóa`; phải chờ khoảng 3 phút.
- **Ảnh:** [login_screen.jpg](screenshots/login_screen.jpg)
