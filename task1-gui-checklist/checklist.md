# GUI Checklist — EShop Web Admin (G5)

Bản AI sinh ban đầu: 79 mục. Nguồn: AI (Claude Opus 5.5).

| ID | IA | Screen | Checklist item | Expected result | Ref | Source | Why AI missed it | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| GUI-01 | IA-01 | Tất cả | Ngôn ngữ giao diện thống nhất tiếng Việt | Mọi nhãn, nút, tiêu đề, thông báo đều tiếng Việt (trừ thuật ngữ chuẩn như Dashboard, CSV) | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-02 | IA-01 | Admin Login | Tiêu đề, placeholder và nút của form đăng nhập bằng tiếng Việt | Hiển thị 'Đăng nhập quản trị', 'Mật khẩu', 'Đăng nhập' thay vì 'Admin Login', 'Password', 'Login' | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-03 | IA-01 | Tất cả | Mỗi màn hình có đúng một thẻ <h1> mô tả nội dung trang | Mỗi màn hình có 1 <h1> là tên màn hình (VD: 'Quản lý Sản phẩm'), không dùng <h1> cho logo | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-04 | IA-01 | Tất cả | Nút hành động tích cực dùng màu xanh dương | Các nút Thêm mới, Lưu sản phẩm, Tạo mã, Xác nhận, Import đều màu xanh dương | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-05 | IA-01 | Tất cả | Nút nguy hiểm/hủy bỏ dùng màu đỏ | Các nút Xóa, Hủy (đơn hàng) đều màu đỏ | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-06 | IA-01 | Tất cả | Đơn vị tiền tệ thống nhất ký hiệu ₫ với phân cách hàng nghìn | Mọi giá trị tiền dạng 1.000.000 ₫, cùng một kiểu dấu phân cách trên mọi màn hình | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-07 | IA-01 | Quản lý Sản phẩm | Cột Giá trong bảng sản phẩm có phân cách hàng nghìn | Giá hiển thị dạng 15.000.000 ₫, không phải 15000000 ₫ | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-08 | IA-01 | Dashboard | Nhãn thẻ thống kê rõ nghĩa, không trộn tiếng Anh | Nhãn 'Tổng doanh thu (đơn đã giao)' thay vì '(Delivered)' | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-09 | IA-01 | Tất cả | Font chữ, cỡ chữ và khoảng cách nhất quán giữa các màn hình | Tiêu đề, bảng, form dùng cùng font và thang cỡ chữ ở mọi tab | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-10 | IA-01 | Tất cả | Tên menu khớp với tiêu đề màn hình tương ứng | Menu 'Mã Giảm Giá' mở màn hình có tiêu đề tương ứng, viết hoa thống nhất | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-11 | IA-01 | Tất cả | Cách viết hoa tiêu đề cột bảng nhất quán | Các cột cùng một kiểu (VD: 'Tên danh mục', không lẫn 'Tên Danh Mục' và 'Tên SP') | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-12 | IA-01 | Tất cả | Không dùng chữ viết tắt khó hiểu trên nhãn | Dùng 'Tên sản phẩm' thay vì 'Tên SP'; nhãn 'Role' được Việt hóa | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-13 | IA-01 | Tất cả | Thứ tự Tab đi từ trên xuống dưới, trái sang phải | Nhấn Tab lần lượt qua menu → tiêu đề → form → bảng theo thứ tự đọc | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-14 | IA-01 | Quản lý Sản phẩm | Ảnh sản phẩm trong bảng có thuộc tính alt mô tả | Mỗi <img> có alt khác rỗng mô tả sản phẩm | FR-24 | AI (Claude Opus 5.5) |  |  |  |
| GUI-15 | IA-01 | Quản lý Sản phẩm | Ảnh thu nhỏ giữ đúng tỷ lệ, không méo | Ảnh 1:1, cắt/thu gọn không làm biến dạng | FR-05 | AI (Claude Opus 5.5) |  |  |  |
| GUI-16 | IA-01 | Tất cả | Độ tương phản chữ và nền đạt WCAG AA | Tỷ lệ tương phản ≥ 4.5:1 cho chữ thường (kể cả menu trên nền tối) | WCAG 2.1 1.4.3 | AI (Claude Opus 5.5) |  |  |  |
| GUI-17 | IA-01 | Tất cả | Bố cục không vỡ ở độ rộng 1366px và 1024px | Bảng, form, sidebar hiển thị đủ, không chồng lấn, không cuộn ngang trang | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-18 | IA-01 | Quản lý Mã giảm giá | Bảng coupon hiển thị loại và giá trị rõ ràng | Loại 'Phần trăm/Cố định' và giá trị '10%' hoặc '50.000 ₫' đúng theo loại | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-19 | IA-02 | Admin Login | Trường Email dùng type="email" | Nhập 'abc' rồi submit thì trình duyệt báo định dạng email không hợp lệ | FR-22 | AI (Claude Opus 5.5) |  |  |  |
| GUI-20 | IA-02 | Admin Login | Trường Mật khẩu dùng type="password" | Ký tự mật khẩu bị che | FR-22 | AI (Claude Opus 5.5) |  |  |  |
| GUI-21 | IA-02 | Tất cả | Mỗi trường nhập có nhãn (label) hiển thị, không chỉ placeholder | Nhãn vẫn còn khi người dùng đã nhập dữ liệu | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-22 | IA-02 | Tất cả | Trường bắt buộc có dấu * bên cạnh nhãn | Các trường bắt buộc (Tên SP, Giá, Danh mục, Mã coupon, Ngày hết hạn...) có * | FR-22 | AI (Claude Opus 5.5) |  |  |  |
| GUI-23 | IA-02 | Quản lý Danh mục | Không cho thêm danh mục với tên rỗng | Bấm 'Thêm mới' khi để trống thì hiện lỗi, không tạo dòng mới | FR-14 | AI (Claude Opus 5.5) |  |  |  |
| GUI-24 | IA-02 | Quản lý Danh mục | Không cho thêm danh mục tên chỉ gồm khoảng trắng | Nhập '   ' thì hiện lỗi, không tạo danh mục rỗng | FR-14 | AI (Claude Opus 5.5) |  |  |  |
| GUI-25 | IA-02 | Quản lý Sản phẩm | Tên sản phẩm là bắt buộc | Để trống Tên thì không lưu được, có thông báo lỗi | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-26 | IA-02 | Quản lý Sản phẩm | Tên sản phẩm tối đa 255 ký tự | Không nhập được quá 255 ký tự hoặc có thông báo lỗi khi vượt | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-27 | IA-02 | Quản lý Sản phẩm | Giá sản phẩm là bắt buộc | Để trống Giá thì không lưu được, có thông báo lỗi | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-28 | IA-02 | Quản lý Sản phẩm | Giá phải là số dương (> 0) | Nhập 0 hoặc -1000 thì bị chặn với thông báo lỗi | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-29 | IA-02 | Quản lý Sản phẩm | Danh mục bắt buộc chọn từ danh sách | Dropdown có lựa chọn mặc định 'Chọn danh mục'; chưa chọn thì không lưu | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-30 | IA-02 | Quản lý Sản phẩm | Bấm 'Sửa' đưa đúng dữ liệu sản phẩm lên form | Form điền đủ tên, giá, ảnh, mô tả, danh mục; tiêu đề đổi thành 'Sửa sản phẩm' | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-31 | IA-02 | Quản lý Sản phẩm | Nút 'Hủy sửa' đưa form về chế độ thêm mới | Form trống, tiêu đề 'Thêm sản phẩm mới', nút 'Hủy sửa' biến mất | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-32 | IA-02 | Import CSV | Chỉ chấp nhận file .csv | Hộp chọn file lọc .csv; chọn file .xlsx/.txt thì hiện lỗi | FR-16 | AI (Claude Opus 5.5) |  |  |  |
| GUI-33 | IA-02 | Import CSV | Có link tải file mẫu với header đúng | File mẫu có header name,price,description,imageUrl,category_id và hiển thị tiếng Việt đúng | FR-16 | AI (Claude Opus 5.5) |  |  |  |
| GUI-34 | IA-02 | Import CSV | Xem trước tách cột đúng với trường có dấu phẩy trong nháy kép | Dòng có description "Áo, quần" hiển thị đúng 1 ô, không lệch cột (RFC 4180) | FR-16 | AI (Claude Opus 5.5) |  |  |  |
| GUI-35 | IA-02 | Quản lý Mã giảm giá | Mã coupon bắt buộc và tự chuyển chữ hoa | Gõ 'save20' hiển thị 'SAVE20'; để trống thì không tạo được | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-36 | IA-02 | Quản lý Mã giảm giá | Giá trị giảm phải là số dương | Nhập 0 hoặc số âm thì bị chặn với thông báo lỗi | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-37 | IA-02 | Quản lý Mã giảm giá | Giá trị phần trăm không vượt quá 100 | Loại Phần trăm, nhập 150 thì bị chặn | FR-17 (logic) | AI (Claude Opus 5.5) |  |  |  |
| GUI-38 | IA-02 | Quản lý Mã giảm giá | Đơn tối thiểu ≥ 0 | Nhập số âm thì bị chặn | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-39 | IA-02 | Quản lý Mã giảm giá | Số lần dùng tối đa/người ≥ 1 | Nhập 0 thì bị chặn | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-40 | IA-02 | Quản lý Mã giảm giá | Không chọn được ngày hết hạn trong quá khứ | Date picker chặn ngày trước hôm nay hoặc báo lỗi | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-41 | IA-02 | Quản lý Mã giảm giá | Mã coupon trùng bị từ chối với thông báo rõ | Tạo lại 'SAVE10' thì hiện 'Mã đã tồn tại' | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-42 | IA-02 | Tất cả | Thông báo lỗi validation xuất hiện phía trên nút submit | Lỗi hiển thị inline trên nút submit, gần trường bị lỗi | FR-22 | AI (Claude Opus 5.5) |  |  |  |
| GUI-43 | IA-02 | Tất cả | Form được reset sau khi submit thành công | Sau khi thêm danh mục/sản phẩm/coupon, các trường trở về trống/mặc định | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-44 | IA-02 | Tất cả | Nhấn Enter trong form sẽ submit | Enter trong ô nhập thực hiện đúng hành động của form | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-45 | IA-03 | Sidebar | Mục menu đang chọn được highlight | Mục tương ứng màn hình hiện tại có màu/nền khác biệt rõ | FR-23 | AI (Claude Opus 5.5) |  |  |  |
| GUI-46 | IA-03 | Sidebar | Mục menu dùng được bằng bàn phím | Tab tới được từng mục menu và Enter/Space mở màn hình | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-47 | IA-03 | Sidebar | Nút đăng xuất có nhãn 'Đăng xuất' | Nhãn đúng 'Đăng xuất', không phải 'Thoát' | FR-23 | AI (Claude Opus 5.5) |  |  |  |
| GUI-48 | IA-03 | Sidebar | Đăng xuất quay về màn hình đăng nhập và không vào lại bằng Back | Sau đăng xuất, nhấn Back không hiển thị dữ liệu admin | FR-12 | AI (Claude Opus 5.5) |  |  |  |
| GUI-49 | IA-03 | Tất cả | Mỗi màn hình có URL riêng | Mỗi tab đổi URL (VD: /products); copy URL mở đúng màn hình | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-50 | IA-03 | Tất cả | Tải lại trang giữ nguyên màn hình đang xem | F5 ở 'Đơn hàng' vẫn ở 'Đơn hàng', không về Dashboard | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-51 | IA-03 | Tất cả | Nút Back của trình duyệt quay về màn hình trước | Từ Sản phẩm sang Đơn hàng, nhấn Back thì về Sản phẩm | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-52 | IA-03 | Tất cả | Có breadcrumb hoặc chỉ dẫn vị trí ở màn hình con | Hiển thị 'Admin / Quản lý Sản phẩm' hoặc tương đương | FR-23 | AI (Claude Opus 5.5) |  |  |  |
| GUI-53 | IA-03 | Admin Login | Tài khoản không phải admin bị chặn với thông báo rõ | Đăng nhập test@eshop.com thì hiện lỗi không có quyền, ở lại trang đăng nhập | FR-12 | AI (Claude Opus 5.5) |  |  |  |
| GUI-54 | IA-03 | Tất cả | Bảng dài có phân trang hoặc cuộn với header cố định | Danh sách nhiều dòng vẫn thấy tiêu đề cột và điều hướng được | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-55 | IA-03 | Quản lý Người dùng | Checkbox chọn tất cả/chọn dòng có chức năng đi kèm | Tick checkbox thì có hành động hàng loạt; tick header chọn tất cả dòng | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-56 | IA-03 | Tất cả | Sau thao tác Sửa, trang cuộn/đưa focus tới form | Bấm 'Sửa' ở cuối bảng thì người dùng thấy ngay form sửa | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-57 | IA-04 | Tất cả | Hiển thị trạng thái loading khi đang tải dữ liệu | Bảng/thẻ thống kê có spinner hoặc skeleton khi chờ API | FR-05 | AI (Claude Opus 5.5) |  |  |  |
| GUI-58 | IA-04 | Tất cả | Bảng trống có empty state với icon và thông điệp | Khi không có dữ liệu hiển thị hình minh họa + thông báo thân thiện | FR-24 | AI (Claude Opus 5.5) |  |  |  |
| GUI-59 | IA-04 | Danh mục / Sản phẩm / Coupon / Người dùng | Thao tác Xóa có hộp thoại xác nhận | Bấm Xóa hiện hộp thoại xác nhận; chọn Hủy thì dữ liệu giữ nguyên | FR-24 | AI (Claude Opus 5.5) |  |  |  |
| GUI-60 | IA-04 | Tất cả | Thao tác thành công có thông báo phản hồi | Thêm/sửa/xóa/đổi trạng thái thành công đều có toast xác nhận | FR-24 | AI (Claude Opus 5.5) |  |  |  |
| GUI-61 | IA-04 | Tất cả | Thông báo lỗi bằng tiếng Việt, dễ hiểu, không lộ lỗi kỹ thuật | Không hiển thị chuỗi như 'Request failed with status code 500' | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-62 | IA-04 | Tất cả | Thông báo dùng toast/inline thay vì hộp alert() của trình duyệt | Không xuất hiện hộp thoại alert mặc định của trình duyệt | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-63 | IA-04 | Quản lý Đơn hàng | Trạng thái đơn được dịch tiếng Việt và phân biệt màu | 5 trạng thái có nhãn tiếng Việt và màu khác nhau | FR-11, FR-18 | AI (Claude Opus 5.5) |  |  |  |
| GUI-64 | IA-04 | Quản lý Đơn hàng | Chỉ hiển thị nút chuyển trạng thái hợp lệ theo state machine | Đơn 'Đã giao' và 'Đã hủy' không có nút hành động nào | FR-10, FR-18 | AI (Claude Opus 5.5) |  |  |  |
| GUI-65 | IA-04 | Quản lý Đơn hàng | Hủy đơn có hộp thoại xác nhận | Bấm 'Hủy' hiện xác nhận trước khi đổi trạng thái | FR-24 | AI (Claude Opus 5.5) |  |  |  |
| GUI-66 | IA-04 | Quản lý Đơn hàng | Nút 'Hủy' đơn hàng dùng màu đỏ | Nút Hủy màu đỏ, phân biệt với nút xác nhận | FR-21 | AI (Claude Opus 5.5) |  |  |  |
| GUI-67 | IA-04 | Quản lý Đơn hàng | Địa chỉ giao hàng hiển thị dạng văn bản an toàn | Địa chỉ chứa '<b>x</b>' hiển thị nguyên văn, không in đậm/không chạy script | FR-18, SEC-04 | AI (Claude Opus 5.5) |  |  |  |
| GUI-68 | IA-04 | Dashboard | Tổng doanh thu chỉ tính đơn đã giao | Giá trị bằng tổng tiền các đơn 'Đã giao' trong tab Đơn hàng | FR-13 | AI (Claude Opus 5.5) |  |  |  |
| GUI-69 | IA-04 | Dashboard | Số liệu cập nhật sau khi đổi trạng thái đơn | Hoàn thành một đơn rồi quay lại Dashboard thì doanh thu tăng đúng | FR-13 | AI (Claude Opus 5.5) |  |  |  |
| GUI-70 | IA-04 | Quản lý Sản phẩm | Sửa một sản phẩm chỉ thay đổi đúng sản phẩm đó | Sau khi lưu, các dòng khác trong bảng giữ nguyên tên | FR-15 | AI (Claude Opus 5.5) |  |  |  |
| GUI-71 | IA-04 | Import CSV | Nút Import vô hiệu khi chưa có file và báo đang xử lý | Nút mờ khi chưa chọn file; khi chạy hiển thị 'Đang import...' | FR-16 | AI (Claude Opus 5.5) |  |  |  |
| GUI-72 | IA-04 | Import CSV | Báo cáo kết quả import rõ ràng | Hiển thị số dòng thành công, số dòng lỗi và lý do từng dòng | FR-16 | AI (Claude Opus 5.5) |  |  |  |
| GUI-73 | IA-04 | Import CSV | Import có dòng lỗi thì rollback toàn bộ và báo rõ | File có 1 dòng giá âm thì không sản phẩm nào được thêm, thông báo nêu dòng lỗi | FR-16 | AI (Claude Opus 5.5) |  |  |  |
| GUI-74 | IA-04 | Quản lý Người dùng | Không cho xóa tài khoản đang đăng nhập | Nút Xóa ở dòng admin hiện tại bị ẩn/vô hiệu hoặc có thông báo từ chối | FR-19 | AI (Claude Opus 5.5) |  |  |  |
| GUI-75 | IA-04 | Quản lý Người dùng | Danh sách người dùng không lộ mật khẩu | Không có cột/giá trị mật khẩu hay hash | FR-19 | AI (Claude Opus 5.5) |  |  |  |
| GUI-76 | IA-04 | Quản lý Mã giảm giá | Coupon hết hạn hiển thị phân biệt nhưng vẫn kèm ngày | Hiển thị nhãn 'Hết hạn' màu đỏ cùng ngày hết hạn | FR-17 | AI (Claude Opus 5.5) |  |  |  |
| GUI-77 | IA-04 | Tất cả | Phần tử tương tác có trạng thái hover và focus nhìn thấy được | Nút/menu đổi màu khi hover; có viền focus khi dùng bàn phím | WCAG 2.1 2.4.7 | AI (Claude Opus 5.5) |  |  |  |
| GUI-78 | IA-04 | Tất cả | Nút submit bị khóa khi đang gửi để tránh bấm hai lần | Bấm nhanh 2 lần 'Thêm mới' chỉ tạo 1 bản ghi | General | AI (Claude Opus 5.5) |  |  |  |
| GUI-79 | IA-04 | Admin Login | Đăng nhập sai có thông báo rõ nhưng không lộ nguyên nhân | Hiện 'Email hoặc mật khẩu không đúng' ngay trên form | FR-02 | AI (Claude Opus 5.5) |  |  |  |
