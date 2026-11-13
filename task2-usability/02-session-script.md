# Kịch bản điều phối buổi kiểm thử (Moderator script)

## 0. Chuẩn bị trước mỗi buổi (5 phút)

1. Khởi động lại backend (backend tự reset database khi khởi động):
   ```bash
   cd "D:/HK1 4 year/Testing course/HW03/eshop-sut/backend" && node server.js
   ```
2. Ở terminal khác, tạo lại 6 đơn mẫu:
   ```bash
   node "D:/HK1 4 year/Testing course/HW03/tools/seed-orders.mjs"
   ```
3. Chạy Web Admin (nếu chưa chạy): `cd eshop-sut/frontend-admin && npm run dev`.
4. Mở Chrome cửa sổ **ẩn danh** tại `http://localhost:5174` (để không còn phiên đăng nhập cũ). Phóng to cửa sổ.
5. Bật ghi màn hình + micro. Chuẩn bị thẻ nhiệm vụ, phiếu SUS, mẫu ghi chú (đặt mã P1…P7).

## 1. Mở đầu (đọc gần như nguyên văn)

> "Cảm ơn anh/chị đã giúp em. Hôm nay em đang thử nghiệm **một trang web quản trị cửa hàng**, không phải kiểm tra anh/chị. Không có câu trả lời đúng hay sai — nếu chỗ nào khó, đó là lỗi của trang web và chính là điều em cần tìm.
>
> Trong lúc làm, anh/chị **nói to suy nghĩ** của mình nhé: đang tìm gì, nghĩ gì, thấy gì lạ. Em sẽ hạn chế trả lời câu hỏi vì muốn xem nếu ở nhà một mình thì anh/chị sẽ làm thế nào.
>
> Em xin phép **ghi hình màn hình và giọng nói** để xem lại, chỉ dùng cho bài tập. Anh/chị đồng ý không ạ?" *(chờ đồng ý — để lời đồng ý có trong video)*

Cho người tham gia làm thử think-aloud 30 giây (VD: "anh/chị thử nói to khi tìm đồng hồ trên màn hình").

## 2. Thực hiện nhiệm vụ

- Đưa **từng thẻ** T1 → T5, đọc to một lần. Bấm giờ khi họ bắt đầu, dừng khi họ nói "xong" hoặc hết thời gian tối đa.
- **Không gợi ý, không giải thích giao diện.** Nếu được hỏi: "Anh/chị thử làm như cách anh/chị nghĩ xem."
- Chỉ can thiệp khi họ **bế tắc hoàn toàn > 1 phút** hoặc hết giờ → ghi "Assist" vào ghi chú, đánh giá P hoặc F.
- Câu nhắc trung lập khi họ im lặng: "Anh/chị đang nghĩ gì?" / "Anh/chị đang tìm gì?"
- Ghi chú theo [04-observation-template.md](04-observation-template.md): ma sát, lỗi, do dự, câu nói bực bội (trích nguyên văn), mốc thời gian video.

## 3. Đóng buổi

1. Đưa **phiếu SUS** (10 câu) — để họ tự điền, không giải thích nghĩa câu hỏi.
2. Hỏi các câu thăm dò ở mục 4, đào sâu vào những chỗ đã quan sát thấy khó.
3. Cảm ơn, hỏi họ có đồng ý để giảng viên gọi xác minh không (nhắc giữ máy).

## 4. Câu hỏi thăm dò (Probe questions)

**Rõ ràng (clarity)**
1. Điều gì trên trang này khó hiểu hoặc gây bất ngờ nhất với anh/chị?
2. Khi tạo sản phẩm / mã giảm giá, anh/chị có biết ô nào bắt buộc, phải nhập kiểu gì không? Vì sao?

**Khôi phục lỗi (error recovery)**
3. Lúc [mô tả lỗi đã quan sát, VD: bấm nhầm Hủy / nhập sai giá], anh/chị biết mình sai bằng cách nào? Anh/chị sửa thế nào?
4. Nếu lỡ bấm Xóa hoặc Hủy nhầm, anh/chị nghĩ trang web sẽ làm gì? Anh/chị có yên tâm không?

**Tốc độ (speed)**
5. Việc nào mất thời gian hơn anh/chị nghĩ? Vì sao?
6. Nếu ngày nào cũng phải làm những việc này, anh/chị muốn trang web làm nhanh hơn ở chỗ nào?

**Tin cậy (trust)**
7. Sau khi bấm Lưu / Tạo mã / Xác nhận, làm sao anh/chị biết việc đó đã thành công?
8. Anh/chị có tin con số doanh thu trên Dashboard không? Vì sao? *(chỉ hỏi sau khi họ đã xong T5)*
9. Anh/chị có dám dùng trang này để quản lý shop thật không? Điều gì sẽ làm anh/chị yên tâm hơn?

**Kết**
10. Nếu được sửa một điều duy nhất, anh/chị sẽ sửa gì?
