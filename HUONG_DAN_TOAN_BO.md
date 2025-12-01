# 📘 HƯỚNG DẪN SỬ DỤNG - HOÀN CHỈNH

## 🎯 Giới thiệu

**Học Chữ Cái** là ứng dụng web học tiếng Việt cho trẻ em, được xây dựng bằng Django (Python).
Ứng dụng có giao diện thân thiện, trò chơi tương tác, và hệ thống theo dõi tiến độ.

---

## 🚀 KHỞI ĐỘNG NHANH (2 phút)

### Bước 1: Mở PowerShell

```powershell
# Tìm PowerShell trên máy tính và mở
```

### Bước 2: Di chuyển vào thư mục

```bash
cd D:\pythonweb
```

### Bước 3: Kích hoạt môi trường

```bash
.venv\Scripts\activate
```

### Bước 4: Khởi động server

```bash
python manage.py runserver
```

### Bước 5: Mở trình duyệt

Vào địa chỉ: **http://127.0.0.1:8000/**

✅ **Xong! Ứng dụng đã sẵn sàng**

---

## 📱 CÁC TRANG CHÍNH

### 🏠 Trang chủ (Home)

- **URL**: http://127.0.0.1:8000/
- **Nội dung**:
  - Danh sách tất cả bài học
  - Nút đăng nhập / đăng ký
  - Thông tin học sinh (nếu đã đăng nhập)
  - Liên kết đến các trò chơi

### 👤 Đăng ký (Register)

- **URL**: http://127.0.0.1:8000/register/
- **Điền thông tin**:
  - Tên đăng nhập (không dấu, không khoảng trắng)
  - Email
  - Mật khẩu
  - Xác nhận mật khẩu
- **Nhấn "Đăng ký"**
- ✅ Tự động đăng nhập sau khi đăng ký

### 🔐 Đăng nhập (Login)

- **URL**: http://127.0.0.1:8000/login/
- **Điền**:
  - Tên đăng nhập
  - Mật khẩu
- **Nhấn "Đăng nhập"**

### 📚 Chi tiết bài học

- **URL**: http://127.0.0.1:8000/lesson/<id>/
- **Nội dung**:
  - Tiêu đề bài
  - Nội dung HTML
  - Hình ảnh
  - Nút "Làm bài tập"

### ✅ Làm bài tập

- **URL**: http://127.0.0.1:8000/quiz/<id>/
- **Nội dung**:
  - Câu hỏi trắc nghiệm
  - Các tùy chọn trả lời
  - Thanh tiến độ
  - Nút "Nộp bài"

### 📊 Xem tiến độ

- **URL**: http://127.0.0.1:8000/progress/
- **Xem**:
  - Phần trăm hoàn thành
  - Số bài học hoàn thành
  - Tổng điểm
  - Số huy hiệu
  - Chi tiết từng bài

### 🏆 Huy hiệu

- **URL**: http://127.0.0.1:8000/badges/
- **Xem**:
  - Huy hiệu đã đạt
  - Huy hiệu chưa mở
  - Điều kiện mở huy hiệu

### 🎮 Trò chơi Đoán từ

- **URL**: http://127.0.0.1:8000/games/hangman/
- **Cách chơi**:
  1. Bấm các nút chữ cái
  2. Đoán được từ = thắng
  3. Sai 6 lần = thua
  4. Bấm "Chơi lại" để tiếp tục

### 🎮 Trò chơi Nối đôi

- **URL**: http://127.0.0.1:8000/games/matching/
- **Cách chơi**:
  1. Bấm một từ ở bên trái
  2. Bấm ảnh/định nghĩa phù hợp ở phải
  3. Nối tất cả = hoàn thành
  4. Bấm "Chơi lại" để tiếp tục

### 🛠️ Quản trị Admin

- **URL**: http://127.0.0.1:8000/admin/
- **Tài khoản mặc định**:
  - Username: `admin`
  - Password: `admin123`
- **Chức năng**:
  - Thêm bài học
  - Thêm câu hỏi
  - Quản lý học sinh
  - Cấp huy hiệu

---

## 👨‍🎓 HƯỚNG DẪN CHO HỌC SINH

### 1️⃣ Đăng ký tài khoản

```
Trang chủ → Nút "Đăng ký" → Điền thông tin → "Đăng ký"
```

### 2️⃣ Đăng nhập

```
Trang chủ → Nút "Đăng nhập" → Nhập tên + mật khẩu → "Đăng nhập"
```

### 3️⃣ Học bài

```
Trang chủ → Chọn bài → Đọc nội dung → "Làm bài tập"
```

### 4️⃣ Làm bài tập

```
Chọn đáp án → Tiếp tục câu hỏi → "Nộp bài" → Xem kết quả
```

### 5️⃣ Chơi trò chơi

```
Trang chủ → Chọn trò chơi → Chơi → "Chơi lại"
```

### 6️⃣ Xem tiến độ

```
Menu → "Tiến độ" → Xem chi tiết
```

### 7️⃣ Xem huy hiệu

```
Menu → "Huy hiệu" → Xem huy hiệu đã đạt
```

### 8️⃣ Đăng xuất

```
Menu → Tên của bạn → "Đăng xuất"
```

---

## 👨‍💼 HƯỚNG DẪN CHO GIÁO VIÊN

### 1️⃣ Truy cập quản trị

```
http://127.0.0.1:8000/admin/
Username: admin
Password: admin123
```

### 2️⃣ Thêm bài học

```
Admin → "Lessons" → "Add Lesson" → Điền thông tin:
  - Title: Tên bài
  - Description: Mô tả ngắn
  - Lesson type: Chọn loại (chữ cái, từ vựng, v.v)
  - Order: Thứ tự
  - Content: Nội dung HTML
→ "Save"
```

### 3️⃣ Thêm câu hỏi

```
Admin → "Questions" → "Add Question" → Điền thông tin:
  - Lesson: Chọn bài học
  - Question text: Câu hỏi
  - Question type: multiple_choice
→ Thêm tùy chọn (Options)
  - Text: Nội dung tùy chọn
  - Is correct: Đánh dấu nếu đúng
→ "Save"
```

### 4️⃣ Cấp huy hiệu

```
Admin → "Badges" → Chọn huy hiệu → Ở "Users" thêm học sinh → "Save"
```

### 5️⃣ Xem tiến độ học sinh

```
Admin → "Student Progresses" → Chọn học sinh → Xem chi tiết
```

### 6️⃣ Xem câu trả lời

```
Admin → "Quiz Answers" → Lọc theo học sinh → Xem chi tiết
```

---

## 📊 BẢNG DỮ LIỆU (Database)

### Models có sẵn:

#### 1. **Lesson** - Bài học

```
- title: Tên bài
- description: Mô tả
- lesson_type: Loại (alphabet|vocabulary|sentences|sounds)
- content: Nội dung HTML
- image: Hình ảnh
- audio: File âm thanh
- order: Thứ tự
```

#### 2. **Question** - Câu hỏi

```
- lesson: Bài học
- question_text: Nội dung câu
- question_type: Loại (multiple_choice|text_input|matching)
- image: Hình ảnh
- order: Thứ tự
```

#### 3. **QuestionOption** - Tùy chọn trả lời

```
- question: Câu hỏi
- text: Nội dung
- is_correct: Đúng?
- image: Hình ảnh
- order: Thứ tự
```

#### 4. **StudentProgress** - Tiến độ học sinh

```
- user: Người dùng
- current_lesson: Bài hiện tại
- total_score: Tổng điểm
- lessons_completed: Bài hoàn thành
```

#### 5. **QuizAnswer** - Câu trả lời

```
- user: Học sinh
- question: Câu hỏi
- selected_option: Tùy chọn
- is_correct: Đúng?
- answered_at: Thời gian
```

#### 6. **Badge** - Huy hiệu

```
- name: Tên huy hiệu
- description: Mô tả
- icon: Hình ảnh
- condition: Điều kiện
- users: Học sinh đạt được
```

---

## 🔧 LỆNH DJANGO HỮU ÍCH

```bash
# Tạo admin mới
python manage.py createsuperuser

# Chạy migrations
python manage.py migrate

# Tạo migrations
python manage.py makemigrations

# Thêm dữ liệu mẫu
python seed_data.py

# Chạy tests
python manage.py test

# Kiểm tra lỗi
python manage.py check

# Collect static files
python manage.py collectstatic

# Shell Django
python manage.py shell

# Reset database
python manage.py flush

# Chạy server trên port khác
python manage.py runserver 8001
```

---

## 🌐 CẤU TRÚC URL

| Path                 | View          | Mô tả         |
| -------------------- | ------------- | ------------- |
| `/`                  | home          | Trang chủ     |
| `/register/`         | register      | Đăng ký       |
| `/login/`            | login_view    | Đăng nhập     |
| `/logout/`           | logout_view   | Đăng xuất     |
| `/lesson/<id>/`      | lesson_detail | Chi tiết bài  |
| `/quiz/<id>/`        | quiz          | Làm bài tập   |
| `/quiz/<id>/submit/` | submit_quiz   | Nộp bài       |
| `/progress/`         | progress      | Xem tiến độ   |
| `/badges/`           | my_badges     | Xem huy hiệu  |
| `/games/hangman/`    | game_hangman  | Chơi Hangman  |
| `/games/matching/`   | game_matching | Chơi Matching |
| `/admin/`            | Django Admin  | Quản trị      |

---

## 🐛 GIẢI QUYẾT VẤN ĐỀ

### Lỗi: "Port 8000 already in use"

```bash
python manage.py runserver 8001
```

### Lỗi: "Database is locked"

```bash
# Xóa database
del db.sqlite3

# Tạo lại
python manage.py migrate
python seed_data.py
```

### Lỗi: "Module not found"

```bash
pip install -r requirements.txt
```

### Lỗi: "CSS/JS không tải"

```bash
python manage.py collectstatic --noinput
```

### Lỗi: "Image không hiển thị"

- Kiểm tra thư mục `media/` tồn tại
- Kiểm tra cài đặt trong `settings.py`
- Kiểm tra quyền truy cập

---

## 📁 CẤU TRÚC THƯ MỤC

```
D:\pythonweb/
│
├── manage.py                 # Django CLI
├── db.sqlite3               # Database
│
├── HocChuCai/               # Cấu hình
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── lessons/                 # App chính
│   ├── models.py            # 7 models
│   ├── views.py             # 10+ views
│   ├── urls.py              # URLs
│   ├── admin.py             # Admin
│   ├── apps.py
│   ├── tests.py             # Tests
│   │
│   ├── templates/lessons/   # 15+ HTML
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── lesson_detail.html
│   │   ├── quiz.html
│   │   ├── quiz_result.html
│   │   ├── progress.html
│   │   ├── badges.html
│   │   └── games/
│   │       ├── hangman.html
│   │       └── matching.html
│   │
│   └── static/              # CSS, JS
│       ├── css/style.css
│       └── js/script.js
│
├── media/                   # User uploads
├── staticfiles/             # Static files
│
├── requirements.txt         # Dependencies
├── seed_data.py            # Sample data
│
├── README.md               # Vietnamese
├── HUONG_DAN.md           # Vietnamese
├── QUICKSTART.md          # Quick start
├── FEATURES.md            # Features
└── SUMMARY.md             # Summary
```

---

## 📚 BÀI HỌC MẪU SẴN CÓ

1. **Chữ A, Â, Ă** - Chữ cái cơ bản
2. **Từ vựng: Động vật** - Các từ về động vật
3. **Câu cơ bản: Giới thiệu** - Lời chào, giới thiệu
4. **Phát âm: Nguyên âm** - Luyện phát âm

---

## 💻 YÊUMẮC CẤU HÌNH

- Python 3.8+
- Django 5.2+
- SQLite (built-in)
- Pillow (xử lý ảnh)

---

## 📞 CẦN GIÚP ĐỠ?

1. **Kiểm tra README.md** - Tài liệu chính
2. **Kiểm tra HUONG_DAN.md** - Hướng dẫn chi tiết
3. **Xem error trong terminal** - Thường có gợi ý
4. **Xem F12 trong browser** - Kiểm tra console
5. **Chạy lệnh check**: `python manage.py check`

---

## 🎓 LƯU Ý QUAN TRỌNG

✅ **Làm được**:

- Tạo bài học trực tiếp từ admin
- Chỉnh sửa bài học bất cứ lúc nào
- Xem tiến độ học sinh chi tiết
- Xóa dữ liệu an toàn

⚠️ **Cần cẩn thận**:

- Xóa database sẽ mất tất cả dữ liệu
- Không xóa file quan trọng
- Không sửa code vô ý

---

## 🎉 CHÚC BẠN SỬ DỤNG VUI VẺ!

Made with ❤️ for Vietnamese children education
Tạo bằng ❤️ cho giáo dục trẻ em Việt Nam

**Happy Learning! Chúc học vui!** 🌟
