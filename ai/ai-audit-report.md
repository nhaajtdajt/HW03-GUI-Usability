# AI Audit Report

**I use AI tools for the following tasks**: đọc và phân tích đề, cài đặt SUT, tạo dữ liệu mẫu, thiết kế GUI checklist bản đầu, thực thi checklist trên trình duyệt, gom bug, soạn bộ tài liệu usability, kế hoạch cross-browser, viết Agent Skills.

| Mục | Giá trị |
|---|---|
| Công cụ | Claude Code (Claude desktop app, tab Code) — model **Claude Sonnet 5.5** (lượt 1–2), **Claude Opus 5.5** (lượt 3 trở đi, đổi bằng `/model`) |
| Ngày | 2026-11-13 (buổi tối) |
| Nhật ký đầy đủ | Bản xuất transcript của phiên Claude Code (đính kèm `ai/transcript.md` — *cần xuất từ app*) |

> Giờ của từng lượt lấy theo transcript xuất ra; bảng dưới ghi thứ tự và tóm tắt output. Output dài (file) được dẫn link thay vì chép lại.

| # | Prompt của tôi (nguyên văn) | Output của AI (tóm tắt) | Tôi đã kiểm tra / sửa gì |
|---|---|---|---|
| 1 | "đọc đề và hiểu các yêu cầu đề đi, đây có phải là bài nhóm không hay là chia cho mỗi người trong nhóm làm mỗi phần" | Đọc PDF 9 trang; tóm tắt 4 task, điểm, yêu cầu chung, nội dung zip; kết luận "Individual Assignment" | Đối chiếu lại mục 1 và mục 5 của đề |
| 2 | "là sao đây là bài nhóm nhưng mỗi người chịu làm mỗi yêu cầu rồi nộp mỗi người riêng chứ không làm hết bài trong đề này" | Giải thích theo đề: mỗi người làm đủ 4 task, nhóm chỉ chia màn hình/flow khác nhau; khuyên hỏi giảng viên | — |
| 3 | (ảnh bảng 5 gói) "tôi được phân công làm phần 5 nè bạn xác định rõ đi rồi mình sẽ làm nhé" | Đọc README đặc tả + code admin qua `gh api`; xác định 7 màn hình admin, flow, nền tảng; chỉ ra Expo Go không có admin | Xác nhận G5 = Web Admin |
| 4 | "Cài và chạy SUT" | Clone repo, `npm install` backend + admin, tạo `.claude/launch.json`, chạy server, đăng nhập thử thành công; phát hiện `setup_guide.md` ghi sai mật khẩu admin | — |
| 5 | "Có, tạo đơn mẫu" | Cài frontend-web; viết `tools/seed-orders.mjs` tạo 6 đơn đủ 5 trạng thái; phát hiện doanh thu Dashboard gấp đôi, đơn đã hủy còn nút giao | — |
| 6 | "Soạn checklist" | Đọc đặc tả FR-21–24 + toàn bộ `App.jsx`; sinh 79 mục (IA-01: 18, IA-02: 26, IA-03: 12, IA-04: 23) bằng `tools/build_checklist.py` → Excel + Markdown | *(Tôi bổ sung các mục AI bỏ sót — Source = Human)* |
| 7 | "cứ hoàn xong giai đoạn này thì tự chấp nhận làm tiếp đi cho tới khi hoàn thành neeis có gì cần tôi cung cấp hay gì đó thì hỏi tôi nhé" | Khởi tạo git; thực thi 79 mục trên Chromium (22 Passed / 57 Failed, 13 ảnh); gom 32 bug (`bug-report.md`); soạn bộ tài liệu Task 2, kế hoạch + overlay + ma trận Task 3, 2 Agent Skills; commit từng bước | *(Tôi xem lại từng kết quả Failed, chạy lại trên Chrome thật)* |

## Những điểm AI làm sai / cần người sửa trong phiên

- Tạo `launch.json` sai thư mục lần đầu (phải chuyển về thư mục gốc HW03).
- Tự làm khóa tài khoản admin 3 phút vì test đăng nhập sai trước các mục khác (thứ tự test chưa hợp lý) — nhưng nhờ vậy phát hiện BUG-32.
- Ảnh chụp không thể hiện được hộp `alert()`/`confirm()` (trình duyệt tích hợp tự đóng hộp thoại) → AI thay `alert` bằng hàm ghi log; nội dung thông báo được ghi trong Notes, cần chụp lại bằng Chrome thật nếu muốn có ảnh hộp thoại.
- Thực thi trên Chromium nhúng trong app, không phải Google Chrome → Task 3 phải chạy lại trên Chrome thật.
- AI đọc code trước khi thiết kế checklist → checklist thiên về những gì AI đã thấy trong code (thiên kiến white-box).
