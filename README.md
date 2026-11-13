# HW03 — GUI & Usability · EShop Web Admin (G5)

**Sinh viên:** _(Họ tên)_ · **MSSV:** _(MSSV)_ · **Email:** _(email sinh viên)_
**Phạm vi (gói G5, không trùng thành viên khác):** màn hình chính **Admin Dashboard**; màn hình phụ Admin Login, Danh mục, Sản phẩm + Import CSV, Mã giảm giá, Đơn hàng, Người dùng. Flow usability: *Đăng nhập Admin → Dashboard → Tạo sản phẩm → Tạo mã giảm giá → Xử lý đơn hàng*.
**SUT:** https://github.com/ttbhanh/eshop-sut (Web Admin `http://localhost:5174`, Backend `http://localhost:3000`).

## Tự đánh giá

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---|---|
| 1 | Task 1 — GUI Checklist (design + execution + bug report) | 30 | |
| 2 | Task 2 — Usability Evaluation (task scenario + 7 sessions + analysis) | 40 | |
| 3 | Task 3 — Cross-Browser / Cross-Platform (≥ 3 platforms) | 20 | |
| 4 | Agent Skills | 10 | |
| | **Total** | **100** | |

## Test summary

| Chỉ số | Giá trị |
|---|---|
| Số màn hình tested (Task 1) | 7 màn hình admin + sidebar |
| Số flow usability (Task 2) | 1 |
| Mục checklist thiết kế | 79 (AI) + _(Human)_ |
| Mục đã thực thi / Passed / Failed (Chromium) | 79 / 22 / 57 |
| Số bug | 32 ([bug-report.md](task1-gui-checklist/bug-report.md)) — trên GitHub Issues: _(link)_ |
| Số người tham gia usability | _(7)_ |
| Điểm SUS trung bình | _(xem SUS_and_Task_Metrics.xlsx)_ |
| Nền tảng cross-browser | Chrome/Windows, Firefox/Windows, Safari/macOS _(hoặc Chrome/Android)_ |
| Demo video Agent Skills | _(link YouTube)_ |

## Cấu trúc bài nộp

| Thư mục / file | Nội dung |
|---|---|
| [task1-gui-checklist/](task1-gui-checklist/) | `GUI_Checklist_G5_Admin.xlsx` (Checklist, Summary, Legend), `checklist.md`, `bug-report.md`, `screenshots/` (ảnh các mục Failed) |
| [task2-usability/](task2-usability/) | Kế hoạch, kịch bản điều phối, thẻ nhiệm vụ + phiếu SUS, mẫu ghi chú, danh sách 7 người, pilot, `SUS_and_Task_Metrics.xlsx`, `sessions/`, phân tích |
| [task3-cross-browser/](task3-cross-browser/) | `plan.md`, `cross_platform_matrix.xlsx`, `screenshots/PF-1..3` |
| [.claude/skills/](.claude/skills/) | Agent Skills `gui-checklist`, `usability-eval` |
| [tools/](tools/) | Script sinh checklist, ghi kết quả, tạo đơn mẫu, bảng SUS, ma trận nền tảng, overlay ảnh |
| [ai/](ai/) | `ai-audit-report.md`, `ai-critique.md` (+ bản PDF) |
| `git-log.txt` | `git log --stat > git-log.txt` trước khi nén |

## Cách chạy lại

```bash
cd eshop-sut/backend && npm install && node server.js        # reset DB mỗi lần khởi động
cd eshop-sut/frontend-admin && npm install && npm run dev
node tools/seed-orders.mjs                                     # 6 đơn mẫu đủ 5 trạng thái
```
