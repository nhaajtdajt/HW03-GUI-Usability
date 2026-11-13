# Task 2 — Kế hoạch đánh giá Usability (G5: Web Admin)

## 1. Mục tiêu (Objectives)

Tìm hiểu một chủ shop online lần đầu dùng EShop Web Admin có tự hoàn thành công việc quản trị hằng ngày được không, và vướng ở đâu.

| # | Câu hỏi nghiên cứu | Đo bằng |
|---|---|---|
| O1 | Người dùng có tìm được đúng chức năng (thống kê, sản phẩm, mã giảm giá, đơn hàng) mà không cần hướng dẫn? | Tỷ lệ hoàn thành, số lần click sai menu, số lần cần trợ giúp |
| O2 | Các form tạo sản phẩm và mã giảm giá có dễ hiểu không (trường nào bắt buộc, nhập định dạng gì)? | Số lỗi nhập, thời gian hoàn thành, câu nói think-aloud |
| O3 | Người dùng có biết thao tác đã thành công hay chưa (phản hồi, trạng thái)? | Số lần kiểm tra lại, thao tác lặp lại, câu hỏi "được chưa?" |
| O4 | Người dùng có khôi phục được khi thao tác nhầm (xóa, hủy, nhập sai)? | Quan sát khi gặp lỗi + câu hỏi thăm dò "khôi phục lỗi" |
| O5 | Người dùng có tin số liệu và thao tác của hệ thống không (doanh thu, đơn hàng)? | Câu hỏi thăm dò "tin cậy", SUS câu 5–6 |
| O6 | Mức độ hài lòng tổng thể | Điểm SUS (mục tiêu ≥ 68 = trung bình ngành) |

## 2. Flow được chọn (không trùng với các bạn trong nhóm)

**Đăng nhập Admin → Xem thống kê Dashboard → Tạo sản phẩm mới → Tạo mã giảm giá → Kiểm tra và xử lý đơn hàng cần xử lý** (FR-12 → FR-19).

## 3. Người tham gia (Target user profile)

- 7 người **ngoài lớp HW03**, ưu tiên **không làm IT / không làm tester**.
- Hồ sơ mục tiêu: đã từng **bán hàng online** (Shopee, Facebook, Zalo…), hoặc làm văn phòng/kế toán/quản lý cửa hàng, có dùng máy tính hằng tuần.
- Chưa từng dùng EShop Admin.
- Có số điện thoại/Zalo/email để TA gọi xác minh (danh sách ghi theo [05-participants.md](05-participants.md), che 4 số giữa).

## 4. Cách thức

- **Moderated**, 1 người/buổi, trực tiếp hoặc qua Google Meet/Zoom (chia sẻ màn hình + điều khiển từ xa).
- Thời lượng mỗi buổi khoảng 30 phút: giới thiệu 3' → làm nhiệm vụ 15–20' → SUS 3' → câu hỏi thăm dò 5–7'.
- Thiết bị: laptop của người kiểm thử, Chrome, Web Admin `http://localhost:5174`.
- **Ghi hình màn hình + âm thanh** (OBS hoặc Xbox Game Bar `Win + Alt + R`) — **xin đồng ý trước**.
- **Trước mỗi buổi phải reset dữ liệu** để mọi người bắt đầu như nhau (xem [02-session-script.md](02-session-script.md) mục 0).

## 5. Kịch bản nhiệm vụ (Task scenario)

Đưa cho người tham gia **thẻ nhiệm vụ** in sẵn ([03-task-cards.md](03-task-cards.md)). Kịch bản nêu **mục tiêu**, không hướng dẫn từng bước.

> **Bối cảnh:** Bạn vừa mở một shop đồ công nghệ online và được cấp tài khoản trang quản trị EShop. Sáng nay bạn cần làm vài việc quen thuộc của chủ shop trước khi mở bán.

| Nhiệm vụ | Thẻ nhiệm vụ (nội dung đưa cho người tham gia) | Tiêu chí thành công | Thời gian tối đa |
|---|---|---|---|
| T1 | Đăng nhập vào trang quản trị bằng tài khoản được cấp. | Vào được màn hình quản trị | 2' |
| T2 | Cho biết hiện tại shop đã có bao nhiêu đơn hàng và doanh thu là bao nhiêu. | Đọc đúng 2 con số trên Dashboard (ghi lại họ có thắc mắc về con số không) | 2' |
| T3 | Bạn nhập về mẫu **Tai nghe Sony WH-1000XM5**, giá bán **8.490.000 ₫**, thuộc nhóm **Phụ kiện**. Hãy đăng bán sản phẩm này. | Sản phẩm xuất hiện trong danh sách với đúng tên, giá, danh mục | 5' |
| T4 | Bạn muốn chạy khuyến mãi: khách có đơn từ **500.000 ₫** được giảm **15%**, mã là **SALE15**, dùng được đến hết **31/12/2026**, mỗi khách chỉ dùng **1 lần**. Hãy tạo mã này. | Mã SALE15 xuất hiện với đúng loại, giá trị, ngưỡng, hạn, số lần | 5' |
| T5 | Một khách vừa gọi điện xin **hủy đơn 30.000.000 ₫** đang chờ xác nhận. Hãy hủy đơn đó, rồi **xác nhận các đơn còn đang chờ** để chuẩn bị giao. | Đơn 30tr ở trạng thái Đã hủy; đơn 101tr ở trạng thái Đã xác nhận; không đơn nào khác bị đổi sai | 5' |

Dữ liệu sau khi reset (từ `tools/seed-orders.mjs`): 6 đơn — #1 30tr (chờ xác nhận), #2 101tr (chờ xác nhận), #3 6tr (đã xác nhận), #4 64tr (đang giao), #5 135tr (đã giao), #6 28tr (đã hủy). Dashboard hiện doanh thu sai (270tr, đúng là 135tr — BUG-04) → quan sát xem người tham gia có phát hiện không, **không gợi ý**.

## 6. Công cụ đo (Instruments)

1. **Ghi chú quan sát có cấu trúc** cho từng buổi: [04-observation-template.md](04-observation-template.md).
2. **SUS** (System Usability Scale, 10 câu, thang 1–5) sau mỗi buổi: [03-task-cards.md](03-task-cards.md#phiếu-sus). Lý do chọn SUS: chuẩn, 10 câu ngắn phù hợp người không làm IT, có ngưỡng so sánh 68 điểm và thang xếp loại.
3. **Câu hỏi mở thăm dò** (sau SUS) bao phủ 4 chủ đề bắt buộc: rõ ràng, khôi phục lỗi, tốc độ, tin cậy — xem [02-session-script.md](02-session-script.md#4-câu-hỏi-thăm-dò-probe-questions).
4. **Bảng tính** [SUS_and_Task_Metrics.xlsx](SUS_and_Task_Metrics.xlsx): tự tính điểm SUS, tỷ lệ hoàn thành, thời gian trung bình.

## 7. Chỉ số (Metrics)

- Hoàn thành nhiệm vụ: **S** (tự làm được) / **P** (làm được sau 1 gợi ý hoặc kết quả có sai nhỏ) / **F** (không làm được hoặc bỏ cuộc).
- Thời gian mỗi nhiệm vụ (giây, xem lại video).
- Số lỗi (click sai, nhập sai, phải làm lại).
- Số lần người điều phối can thiệp.
- Điểm SUS từng người, trung bình, trung vị.

## 8. Pilot

Chạy 1 buổi thử với 1 người (không tính vào 7 người) để kiểm tra: thẻ nhiệm vụ có rõ không, có bước nào hỏng không, thời lượng có vừa không. Ghi lại thay đổi vào [06-pilot-notes.md](06-pilot-notes.md) trước khi chạy buổi thật.

## 9. Đạo đức & quyền riêng tư

- Giải thích mục đích, xin đồng ý ghi hình bằng lời (ghi lại trong video) hoặc ký phiếu.
- Chỉ công khai tên + số điện thoại đã che 4 số giữa (VD: `0912345678` → ghi `091****678`).
- Người tham gia có thể dừng bất cứ lúc nào.
