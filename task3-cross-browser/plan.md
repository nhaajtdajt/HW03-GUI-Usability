# Task 3 — Cross-Browser / Cross-Platform (G5: Web Admin)

Chạy lại GUI checklist của Task 1 ([79 mục](../task1-gui-checklist/checklist.md)) trên **3 nền tảng**, ghi kết quả vào [cross_platform_matrix.xlsx](cross_platform_matrix.xlsx).

> App mobile (Expo Go) **không có phần quản trị**, nên G5 không dùng Expo Go thay một nền tảng được.

## Nền tảng

| # | Nền tảng | Cách chạy | Ghi chú |
|---|---|---|---|
| PF-1 | **Chrome** (bản mới nhất) / Windows 11 | Máy của bạn | Lần chạy Task 1 dùng Chromium trong Claude desktop; chạy lại trên Chrome thật để có ảnh kèm overlay |
| PF-2 | **Firefox** (bản mới nhất) / Windows 11 hoặc Windows 10 | Máy của bạn hoặc BrowserStack Live | Hiển thị `type=number`, `type=date`, `alert()` khác Chromium |
| PF-3 | **Safari** (17/18) / macOS Sonoma hoặc Sequoia | **BrowserStack Live** + Local tunnel | Nếu hết lượt trial: thay bằng **Chrome / Android** (BrowserStack Real Device hoặc điện thoại thật cùng Wi-Fi) |

## Thiết lập BrowserStack Live với localhost

1. Đăng ký trial tại browserstack.com (tự đăng ký, dùng email của bạn).
2. Chạy backend + Web Admin trên máy (`node server.js`, `npm run dev`).
3. Bật **BrowserStack Local**: cài app "BrowserStack Local" (hoặc extension Chrome) rồi bật kết nối, hoặc chạy binary:
   ```bash
   BrowserStackLocal.exe --key <ACCESS_KEY>
   ```
4. Vào **Live** → chọn macOS + Safari → mở `http://localhost:5174`. Backend `http://localhost:3000` cũng đi qua tunnel.
5. Với Android thật cùng Wi-Fi: chạy Vite với `npm run dev -- --host`, mở `http://<IP-LAN>:5174`. **Lưu ý:** admin gọi API ở `http://localhost:3000` (cố định trong code), nên trên điện thoại thật API sẽ lỗi — dùng BrowserStack (có tunnel) cho Android thì ổn hơn.

## Overlay thông tin sinh viên trên ảnh

- File `eshop-sut/frontend-admin/public/tester-overlay.js` (bản sao lưu: [tools/tester-overlay.js](../tools/tester-overlay.js)) đã được gắn vào `index.html` của Web Admin.
- Góc dưới phải mọi màn hình hiển thị: **email sinh viên | MSSV | họ tên | trình duyệt + phiên bản / hệ điều hành | URL | thời gian**.
- Ảnh chụp toàn màn hình (gồm cả thanh địa chỉ nếu có thể) → overlay chứng minh trình duyệt, OS và URL localhost.
- Muốn đổi thông tin: sửa 3 giá trị trong biến `STUDENT` ở đầu file.

## Quy trình mỗi nền tảng

1. Reset dữ liệu (khởi động lại backend + `node tools/seed-orders.mjs`).
2. Thực hiện từng mục checklist theo cột *Expected result*; ghi **Passed/Failed** vào cột của nền tảng trong ma trận.
3. Chụp ảnh **mỗi màn hình chính** (Login, Dashboard, Danh mục, Sản phẩm, Mã giảm giá, Đơn hàng, Người dùng) + **mỗi mục Failed khác Chrome**. Lưu vào `screenshots/<PF>/` với tên `<PF>_<màn hình hoặc GUI-xx>.png`.
4. Cột *Khác biệt* ghi những gì hiển thị/hành vi khác nền tảng còn lại (VD: date picker, spinner số, font, alert).

## Mục cần chú ý vì dễ khác nhau giữa trình duyệt

| Mục | Vì sao |
|---|---|
| GUI-19, GUI-25, GUI-39 | Thông báo validation HTML5 do trình duyệt tự hiển thị, nội dung/vị trí khác nhau |
| GUI-28, GUI-36–38 | `type=number`: Firefox/Safari cho gõ chữ, nút tăng giảm khác |
| GUI-40 | `type=date`: Safari macOS cũ không có date picker |
| GUI-13, GUI-46, GUI-77 | Safari mặc định không cho Tab tới nút (cần bật "Press Tab to highlight each item") |
| GUI-16, GUI-09 | Font hệ thống khác (Segoe UI / San Francisco / Roboto) |
| GUI-32 | Hộp chọn file của macOS/Android khác Windows |
| GUI-62 | Giao diện `alert()` khác nhau; Safari chặn alert lặp lại |
| GUI-17 | Kích thước màn hình Android nhỏ → kiểm tra bố cục nếu PF-3 là Android |
