# HW03 — GUI & Usability: Báo cáo chính

**Sinh viên:** Trương Nhật Đạt · **MSSV:** 23120231 · **Email:** 23120231@student.hcmus.edu.vn \
**SUT:** EShop — Web Admin (`http://localhost:5174`), repo https://github.com/ttbhanh/eshop-sut \
**Phạm vi (gói G5 của nhóm):** màn hình chính **Admin Dashboard**; màn hình phụ Admin Login, Quản lý Danh mục, Quản lý Sản phẩm + Import CSV, Quản lý Mã giảm giá, Quản lý Đơn hàng, Quản lý Người dùng. \
**Repo bài làm & bug:** https://github.com/nhaajtdajt/HW03-GUI-Usability · [Issues #1–#32](https://github.com/nhaajtdajt/HW03-GUI-Usability/issues)

---

## 1. Môi trường

| Thành phần | Giá trị |
|---|---|
| Máy | Windows 11 Home 10.0.26200, Node.js 22.20 |
| SUT | Backend Express + SQLite (reset dữ liệu mỗi lần khởi động), Web Admin React + Vite |
| Dữ liệu mẫu | Seed mặc định + 6 đơn hàng đủ 5 trạng thái tạo bằng [tools/seed-orders.mjs](tools/seed-orders.mjs) |
| Tài khoản | `admin@eshop.com` / `Admin123!` (lưu ý: `setup_guide.md` của SUT ghi sai là `admin123`) |
| Trình duyệt Task 1 | Chromium 156 (trình duyệt tích hợp trong Claude desktop), viewport 1024×768 |
| AI | Claude Code (Claude Sonnet 5.5 → Claude Opus 5.5) — chi tiết ở [AI Audit Report](ai/ai-audit-report.md) |

---

## 2. Task 1 — GUI Checklist

### 2.1 Quy trình (dùng AI theo từng bước của kỹ thuật)

1. **Thu thập yêu cầu giao diện:** AI đọc đặc tả (README của SUT) và trích các yêu cầu GUI FR-21 → FR-24 cùng ràng buộc của FR-12 → FR-19; sau đó mở từng màn hình admin để liệt kê form, bảng, nút, hộp thoại.
2. **Sinh bản checklist đầu:** AI sinh 79 mục theo 4 nhóm IA, mỗi mục có *Expected result* quan sát được và nguồn tham chiếu (FR / General / WCAG) — [tools/build_checklist.py](tools/build_checklist.py).
3. **Review của sinh viên & bổ sung mục AI bỏ sót:** xem mục 2.3.
4. **Thực thi:** chạy từng mục trên trình duyệt; mục đo được thì đo bằng DOM/JS (số thẻ `h1`, `input.type`, `label`, thuộc tính `required/min/maxLength/accept`, tỷ lệ tương phản theo công thức WCAG, thứ tự Tab, `history.length`), mục hành vi thì thao tác thật (click, gõ phím, tải file CSV). Hộp `alert()/confirm()` được ghi log để đọc nội dung (`confirm` trả về *Hủy* để tránh xóa nhầm). Mục Failed được chụp ảnh — [tools/apply_results.py](tools/apply_results.py).
5. **Gom bug:** các mục Failed cùng nguyên nhân gộp thành 1 bug, xếp mức độ, đăng lên GitHub Issues kèm ảnh.

### 2.2 Độ phủ và kết quả

| Interface Aspect | Số mục | Passed | Failed |
|---|---|---|---|
| IA-01 General UI standards | 18 | 5 | 13 |
| IA-02 Forms | 26 | 9 | 17 |
| IA-03 Navigation | 12 | 4 | 8 |
| IA-04 Feedback / state | 23 | 4 | 19 |
| **Tổng (bản AI)** | **79** | **22** | **57** |
| Mục bổ sung (AI soạn, **chờ sinh viên duyệt**) | 5 | 0 | 5 |

Checklist đầy đủ (ID, IA, màn hình, mục kiểm tra, kết quả mong đợi, tham chiếu, nguồn, kết quả, ghi chú, ảnh): [GUI_Checklist_G5_Admin.xlsx](task1-gui-checklist/GUI_Checklist_G5_Admin.xlsx) · [checklist.md](task1-gui-checklist/checklist.md). Ảnh các mục Failed: [task1-gui-checklist/screenshots/](task1-gui-checklist/screenshots/).

**Nhận xét chính**
- Web Admin gần như **không có phản hồi trạng thái**: không loading, không empty state, không thông báo thành công, mọi lỗi qua `alert()`; xóa/hủy không có xác nhận (IA-04 tỷ lệ fail cao nhất, 19/23).
- **Validation form gần như không có**: giá rỗng/0/âm, tên 300 ký tự, coupon 150%, ngày quá khứ, danh mục tên rỗng đều lưu được (IA-02).
- **Điều hướng kiểu state**: mọi màn hình chung một URL, F5 về Dashboard, Back rời ứng dụng; sidebar không dùng được bằng bàn phím (IA-03).
- **Sai nhất quán so với đặc tả GUI**: tiếng Anh lẫn tiếng Việt, màu nút sai quy ước, tiền tệ 3 kiểu định dạng, không có `h1` cho tiêu đề trang, độ tương phản thấp (IA-01).
- Bắt gặp kèm 2 lỗi nghiêm trọng ngoài GUI: **XSS** ở địa chỉ giao hàng và **admin tự xóa được chính mình**.

### 2.3 Mục AI bỏ sót (sinh viên bổ sung)

> **5 mục dưới do AI soạn và đã chạy thử trên Chromium (bản nháp). Sinh viên cần đọc lại, sửa cột "Vì sao AI bỏ sót" bằng lời của mình và có thể thêm mục riêng** (Source = `Human` trong sheet *Checklist*). Ảnh: `task1-gui-checklist/screenshots/extra_*.jpg`; GUI-80, 81, 84 đo bằng DOM nên không có ảnh.

| ID | IA | Mục bổ sung | Vì sao AI bỏ sót (prompt / giới hạn model / đặc thù giao diện) | Kết quả |
|---|---|---|---|---|
| GUI-80 | IA-01 | Tiêu đề tab trình duyệt mô tả đúng từng màn hình | Prompt chỉ nhắc thẻ `h1`; `<title>` là metadata nằm ngoài khung nhìn | Failed (`title` = frontend-admin) |
| GUI-81 | IA-01 | Thuộc tính `lang` khớp ngôn ngữ giao diện | Markup ẩn trong index.html, AI chỉ xét thứ nhìn thấy và code React | Failed (`lang` = en) |
| GUI-82 | IA-01 | Chế độ tối không làm hỏng hiển thị | Đề bài nêu sẵn dark mode là điểm AI hay quên; prompt gốc không yêu cầu theme | Failed (không hỗ trợ) |
| GUI-83 | IA-01 | Bố cục dùng được ở 640px (≈ zoom 200%) | AI chỉ xét kích thước desktop mặc định | Failed (mất cột Hành động) |
| GUI-84 | IA-03 | Có landmark `nav`/`main`/`header` | Giao diện nhìn đúng nên AI không thấy; cần xem cây DOM | Failed (0 landmark) |

### 2.4 Bug report

32 bug: 2 Critical, 6 High, 13 Medium, 11 Low — chi tiết bước tái hiện ở [bug-report.md](task1-gui-checklist/bug-report.md), đã đăng tại [GitHub Issues #1–#32](https://github.com/nhaajtdajt/HW03-GUI-Usability/issues).

| Mức độ | Bug |
|---|---|
| Critical | BUG-01 XSS ở địa chỉ giao hàng · BUG-02 admin tự xóa tài khoản đang đăng nhập |
| High | BUG-03 xóa/hủy không xác nhận · BUG-04 doanh thu gấp đôi · BUG-05 đơn đã hủy vẫn "Đánh dấu Đã giao" · BUG-06 sửa 1 sản phẩm hiển thị đổi tên tất cả · BUG-07 import CSV không rollback · BUG-08 form sản phẩm không validate giá/tên |
| Medium | BUG-09 → BUG-19, BUG-21, BUG-32 |
| Low | BUG-20, BUG-22 → BUG-31 |

---

## 3. Task 2 — Usability Evaluation

### 3.1 Thiết kế

- **Flow (G5, không trùng nhóm):** Đăng nhập Admin → Xem Dashboard → Tạo sản phẩm → Tạo mã giảm giá → Xử lý đơn hàng.
- **Mục tiêu:** O1 tìm đúng chức năng; O2 hiểu form; O3 biết thao tác đã thành công; O4 khôi phục lỗi; O5 tin số liệu; O6 hài lòng tổng thể (SUS ≥ 68). Chi tiết: [01-plan.md](task2-usability/01-plan.md).
- **Kịch bản:** "Bạn vừa mở shop đồ công nghệ online…" với 5 nhiệm vụ theo mục tiêu (đăng nhập, đọc doanh thu, đăng bán tai nghe 8.490.000 ₫, tạo mã SALE15 giảm 15% đơn từ 500.000 ₫, hủy đơn 30 triệu và xác nhận đơn còn chờ) — [03-task-cards.md](task2-usability/03-task-cards.md).
- **Công cụ đo:** SUS 10 câu (tiếng Việt) + 10 câu hỏi thăm dò về rõ ràng, khôi phục lỗi, tốc độ, tin cậy — [02-session-script.md](task2-usability/02-session-script.md); ghi chú có cấu trúc — [04-observation-template.md](task2-usability/04-observation-template.md); tính điểm — [SUS_and_Task_Metrics.xlsx](task2-usability/SUS_and_Task_Metrics.xlsx).
- **Người tham gia:** 7 người ngoài lớp, ưu tiên người bán hàng online / không làm IT — [05-participants.md](task2-usability/05-participants.md). Pilot: [06-pilot-notes.md](task2-usability/06-pilot-notes.md).

### 3.2 Kết quả

> Điền sau khi chạy đủ 7 buổi; phân tích chi tiết ở [07-analysis.md](task2-usability/07-analysis.md).

| Chỉ số | Giá trị |
|---|---|
| SUS trung bình / trung vị | _ / _ |
| Tỷ lệ hoàn thành T1–T5 | _ |
| Phát hiện mức 4 (chặn nhiệm vụ) | _ |

---

## 4. Task 3 — Cross-Browser / Cross-Platform

Chạy lại checklist Task 1 trên 3 nền tảng (Chrome/Windows, Firefox/Windows, Safari/macOS qua BrowserStack — hoặc Chrome/Android). App mobile không có phân hệ admin nên không dùng Expo Go. Mọi ảnh có overlay *email · MSSV · họ tên · trình duyệt/OS · URL · thời gian* ([tools/tester-overlay.js](tools/tester-overlay.js)). Kế hoạch: [plan.md](task3-cross-browser/plan.md) · ma trận: [cross_platform_matrix.xlsx](task3-cross-browser/cross_platform_matrix.xlsx).

| Nền tảng | Đã chạy | Passed | Failed | Khác biệt đáng chú ý |
|---|---|---|---|---|
| PF-1 Chrome 157 / Windows 11 (2026-11-14, 1536×730) | 79 | 22 | 57 | Kết quả giống hệt lần chạy Chromium ở Task 1; ảnh có overlay ở `task3-cross-browser/screenshots/PF-1/` (18 ảnh) |
| PF-2 Firefox 160 / Windows 11 (2026-11-14) | 79 | 22 | 57 | Kết quả giống Task 1; chỉ khác control gốc của Firefox (ô số luôn hiện nút tăng/giảm, select nền xám, date picker, câu thông báo HTML5). Chạy bằng [tools/firefox-pf2.mjs](tools/firefox-pf2.mjs) qua WebDriver BiDi; 18 ảnh overlay ở `task3-cross-browser/screenshots/PF-2/` |
| PF-3 Safari 16.5.1 / macOS (BrowserStack Live, 2026-11-15) | 6 | 1 | 5 | **Chưa đủ.** Trial chỉ cho 1 phút mỗi phiên bản trình duyệt và bàn phím từ xa làm mất ký tự Shift (`@` thành `2`), nên chỉ chụp được trang đăng nhập và hộp `alert()` thật của Safari; 73 mục còn lại ghi N/A. Safari mở được qua Cloudflare Quick Tunnel (BrowserStack Local không nối được). Ảnh: `task3-cross-browser/screenshots/PF-3/` |

---

## 5. Agent Skills

| Skill | Chức năng | Demo |
|---|---|---|
| [gui-checklist](.claude/skills/gui-checklist/SKILL.md) | Đọc yêu cầu → sinh checklist > 40 mục → thực thi bằng browser tool (kèm mẹo đo DOM, ghi log alert/confirm, upload file) → ghi kết quả + ảnh → gom bug | [YouTube: Demo gui-checklist](https://youtu.be/EVDe7BGZ3ZA) |
| [usability-eval](.claude/skills/usability-eval/SKILL.md) | Soạn kế hoạch, kịch bản, SUS, mẫu ghi chú → hướng dẫn chạy buổi → phân tích, nhóm pain point, xếp severity | [YouTube: Demo usability-eval](https://youtu.be/lPESf1FE-rk) |

---

## 6. Phụ lục

- AI Audit Report: [ai/ai-audit-report.md](ai/ai-audit-report.md) · AI Critique: [ai/ai-critique.md](ai/ai-critique.md)
- Git commit log: `git-log.txt`
- Ảnh trang GitHub Issues: `task1-gui-checklist/screenshots/github_issues_page.jpg`
- Self-assessment & test summary: [README.md](README.md)
