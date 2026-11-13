# AI Critique (200–300 từ)

> **BẢN NHÁP do AI viết từ những gì xảy ra trong phiên làm việc.** Đề yêu cầu đây là đánh giá của bạn — hãy đọc, giữ ý nào đúng với trải nghiệm của bạn và **viết lại bằng lời của mình** (đề cấm sao chép, kể cả prompt).

AI giúp tôi đi rất nhanh ở phần cơ học: đọc đặc tả, sinh 79 mục checklist, đo độ tương phản và thứ tự Tab bằng JavaScript, gom 57 mục Failed thành 32 bug. Nhưng nó sai hoặc thiếu ở nhiều chỗ cần phán đoán.

Thứ nhất, AI hiểu sai bối cảnh: lúc đầu nó khẳng định bài "hoàn toàn cá nhân" mà chưa hỏi nhóm tôi chia việc thế nào; chỉ khi tôi gửi bảng phân công nó mới nhận ra nhóm chia theo màn hình/flow. Thứ hai, AI đọc code trước khi viết checklist, nên nhiều mục được "đặt hàng" theo lỗi nó đã thấy trong `App.jsx` — đó là thiên kiến white-box, làm checklist trông đầy đủ nhưng lệch khỏi góc nhìn người dùng; các khía cạnh như dark mode, zoom 200%, tiêu đề tab trình duyệt, thuộc tính `lang` thì nó bỏ qua. Thứ ba, AI lên thứ tự test kém: nó thử đăng nhập sai trước, tự khóa tài khoản admin 3 phút. Thứ tư, nó chạy trên Chromium nhúng và không chụp được hộp `alert()`, nên bằng chứng cho vài mục chỉ là ghi chú chữ.
Nguyên nhân chung: AI tối ưu cho "hoàn thành nhiều mục" chứ không cho "đúng mục đích", và nó chỉ biết những gì nằm trong prompt và trong code nó đọc được.

Nguyên tắc tôi rút ra: giao cho AI phần lặp lại và đo đạc, còn tôi giữ quyền quyết định phạm vi, thứ tự test và tiêu chí Passed/Failed; luôn tự chạy lại các mục quan trọng trên môi trường thật trước khi tin kết quả.
