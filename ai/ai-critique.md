# AI Critique (289 từ)

Trong quá trình làm bài, AI hỗ trợ tôi rất nhanh ở khâu cơ học như sinh checklist, đo độ tương phản hay gom lỗi. Tuy nhiên, AI bộc lộ ba hạn chế lớn về mặt phán đoán. Đầu tiên là thiên kiến "white-box": do đọc trước mã nguồn `App.jsx`, AI có xu hướng đặt kỳ vọng theo những gì code đã viết thay vì góc nhìn người dùng thực tế; nó bỏ sót hoàn toàn các yêu cầu trải nghiệm như dark mode, zoom 200% hay thẻ tiêu đề trình duyệt. Thứ hai, AI lập kế hoạch thực thi rất ngây thơ: nó chạy thử ca đăng nhập sai trước, khiến tài khoản admin bị khóa 3 phút và làm gián đoạn toàn bộ luồng kiểm thử. Thứ ba, ở Task 2, AI không thể thay thế con người cảm nhận sự hoang mang khi bấm nhầm nút hủy đơn mà không có cảnh báo.

Nguyên nhân cốt lõi là AI chỉ suy diễn dựa trên văn bản và mã nguồn có sẵn, thiếu hoàn toàn mô hình tâm lý người dùng (mental model) và trải nghiệm thế giới thực. Nó tối ưu hóa số lượng checklist thay vì chất lượng thực tế.

Bài học lớn nhất tôi rút ra khi cộng tác với AI là nguyên tắc "Human-in-the-loop": xem AI như một trợ lý thực thi tốc độ cao nhưng thụ động. Sinh viên bắt buộc phải giữ vai trò nhạc trưởng — định hướng phạm vi, phản biện giả định, kiểm soát thứ tự thực thi và trực tiếp kiểm chứng trên môi trường thật. Không bao giờ giao phó toàn bộ bài test cho AI nếu không muốn nhận lại một kết quả bề nổi.
