# 🎓 Học Chữ Cái - Ứng dụng học tiếng Việt cho bé

Một ứng dụng web tương tác được xây dựng bằng Django, giúp trẻ em học tiếng Việt một cách vui vẻ và hiệu quả.

## ✨ Tính năng chính

### 📚 Bài học

- **Chữ cái**: Học các chữ cái và phát âm cơ bản
- **Từ vựng**: Học các từ mới với hình ảnh và mô tả
- **Câu cơ bản**: Học cách ghép từ thành câu
- **Phát âm**: Luyện tập phát âm đúng

### 🎮 Trò chơi tương tác

- **Đoán từ (Hangman)**: Trò chơi đoán chữ cái để tìm ra từ bí ẩn
- **Nối đôi (Matching)**: Nối từ với ảnh hoặc định nghĩa tương ứng

### 📊 Theo dõi tiến độ

- Xem số bài học đã hoàn thành
- Theo dõi tổng điểm
- Nhận huy hiệu thành tích

### 🏆 Hệ thống huy hiệu

- Nhận huy hiệu khi hoàn thành bài học
- Động lực học tập qua các thành tích

### 👤 Quản lý tài khoản

- Đăng ký tài khoản mới
- Đăng nhập an toàn
- Theo dõi tiến độ cá nhân

## 🚀 Cài đặt

### Yêu cầu

- Python 3.8+
- Django 5.2+
- Pillow (xử lý hình ảnh)

### Các bước cài đặt

1. **Clone hoặc tạo thư mục dự án**

```bash
cd D:\pythonweb
```

2. **Tạo virtual environment (nếu chưa có)**

```bash
python -m venv .venv
```

3. **Kích hoạt virtual environment**

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. **Cài đặt dependencies**

```bash
pip install -r requirements.txt
```

5. **Chạy migrations**

```bash
python manage.py migrate
```

6. **Tạo tài khoản admin (nếu chưa có)**

```bash
python manage.py createsuperuser
```

7. **Thêm dữ liệu mẫu (nếu muốn)**

```bash
python seed_data.py
```

8. **Chạy server**

```bash
python manage.py runserver
```

9. **Truy cập ứng dụng**

- Trang chủ: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📖 Hướng dẫn sử dụng

### Cho học sinh

1. **Đăng ký**: Bấm "Đăng ký" và điền thông tin
2. **Đăng nhập**: Dùng tài khoản để đăng nhập
3. **Chọn bài học**: Bấm vào bài học để xem nội dung
4. **Làm bài tập**: Trả lời các câu hỏi để kiểm tra kiến thức
5. **Chơi trò chơi**: Luyện tập thêm qua các trò chơi
6. **Xem tiến độ**: Theo dõi tiến độ học tập của mình

### Cho quản trị viên

1. **Truy cập admin**: Đăng nhập tại `/admin/`
2. **Quản lý bài học**:
   - Thêm bài học mới
   - Sửa nội dung bài học
   - Xóa bài học không cần thiết
3. **Quản lý câu hỏi**:
   - Thêm câu hỏi cho các bài học
   - Tạo các tùy chọn trả lời
4. **Theo dõi học sinh**:
   - Xem tiến độ học tập
   - Xem kết quả bài kiểm tra
   - Cấp huy hiệu cho học sinh

## 🏗️ Cấu trúc dự án

```
HocChuCai/
├── HocChuCai/              # Cấu hình chính
│   ├── settings.py         # Cài đặt Django
│   ├── urls.py            # Định tuyến chính
│   ├── wsgi.py
│   └── asgi.py
├── lessons/               # Ứng dụng chính
│   ├── models.py          # Mô hình dữ liệu
│   ├── views.py           # Xử lý logic
│   ├── urls.py            # Định tuyến app
│   ├── admin.py           # Quản lý admin
│   ├── templates/         # Các template HTML
│   │   └── lessons/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── lesson_detail.html
│   │       ├── quiz.html
│   │       ├── quiz_result.html
│   │       ├── progress.html
│   │       ├── badges.html
│   │       └── games/
│   │           ├── hangman.html
│   │           └── matching.html
│   └── static/            # CSS, JS, hình ảnh
│       ├── css/
│       └── js/
├── manage.py              # Django management
├── requirements.txt       # Dependencies
├── seed_data.py          # Script thêm dữ liệu mẫu
└── db.sqlite3            # Database
```

## 🎨 Thiết kế giao diện

- **Màu sắc**: Gradient từ xanh (667eea) đến tím (764ba2)
- **Font**: Comic Sans MS, Segoe UI (thân thiện với trẻ em)
- **Layout**: Responsive, hoạt động tốt trên điện thoại

## 📝 Models

### Lesson (Bài học)

- title: Tên bài học
- description: Mô tả
- lesson_type: Loại bài (chữ cái, từ vựng, câu, phát âm)
- content: Nội dung HTML
- image: Hình ảnh bài học
- audio: File âm thanh

### Question (Câu hỏi)

- lesson: Bài học chứa câu hỏi
- question_text: Nội dung câu hỏi
- question_type: Loại câu hỏi (chọn đáp án, nhập text, nối đôi)
- image: Hình ảnh câu hỏi

### QuestionOption (Tùy chọn trả lời)

- question: Câu hỏi liên quan
- text: Nội dung tùy chọn
- is_correct: Có phải đáp án đúng không
- image: Hình ảnh tùy chọn

### StudentProgress (Tiến độ học sinh)

- user: Tài khoản học sinh
- current_lesson: Bài học hiện tại
- total_score: Tổng điểm
- lessons_completed: Bài học đã hoàn thành

### QuizAnswer (Câu trả lời)

- user: Học sinh
- question: Câu hỏi
- selected_option: Tùy chọn được chọn
- is_correct: Trả lời đúng hay sai

### Badge (Huy hiệu)

- name: Tên huy hiệu
- description: Mô tả
- icon: Hình ảnh huy hiệu
- users: Học sinh đạt được huy hiệu

## 🔧 Tùy chỉnh

### Thêm bài học mới

1. Vào trang admin: `/admin/`
2. Nhấn "Add Lesson"
3. Điền thông tin bài học
4. Thêm câu hỏi từ bước 1 hoặc thêm qua admin sau

### Chỉnh sửa nội dung

- Sửa nội dung trong templates (HTML/CSS)
- Cập nhật dữ liệu qua admin Django

## 🐛 Troubleshooting

### Lỗi Pillow không được cài đặt

```bash
pip install Pillow
```

### Database bị lỗi

```bash
python manage.py migrate --fake-initial
```

### Port 8000 đang sử dụng

```bash
python manage.py runserver 8001
```

## 📧 Liên hệ & Hỗ trợ

Nếu gặp vấn đề, vui lòng kiểm tra:

- Đã cài đặt đủ dependencies chưa?
- Django version có phù hợp không?
- Database có khớp không?

## 📄 License

Dự án này được tạo cho mục đích giáo dục.

## 🎯 Tương lai

- [ ] Thêm audio/phát âm cho các từ
- [ ] Tích hợp text-to-speech
- [ ] Thêm trò chơi tương tác khác
- [ ] Hệ thống leaderboard
- [ ] Mobile app
- [ ] Xuất báo cáo tiến độ
- [ ] Tích hợp AI để tạo bài học tự động

---

**Made with ❤️ for Vietnamese kids learning** 🇻🇳
