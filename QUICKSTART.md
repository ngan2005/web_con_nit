# 🚀 HƯỚNG DẪN KHỞI ĐỘNG NHANH

## ⚡ 30 giây để khởi động

```bash
# 1. Mở PowerShell
# 2. Di chuyển vào thư mục
cd D:\pythonweb

# 3. Kích hoạt virtual environment
.venv\Scripts\activate

# 4. Khởi chạy server
python manage.py runserver
```

✅ **Hoàn thành!** Vào http://127.0.0.1:8000/

---

## 📋 Tài khoản mặc định

### Học sinh

- **Tên**: Tạo tài khoản mới tại trang đăng ký
- **Email**: Email bất kỳ
- **Mật khẩu**: Tự chọn

### Admin (Quản trị)

- **Tên**: `admin`
- **Mật khẩu**: `admin123`
- **Link**: http://127.0.0.1:8000/admin/

---

## 📚 Bài học mẫu sẵn có

1. **Chữ A, Â, Ă** - Học chữ cái cơ bản
2. **Từ vựng: Động vật** - Tên các động vật
3. **Câu cơ bản: Giới thiệu** - Lời chào, tên
4. **Phát âm: Nguyên âm** - Các nguyên âm tiếng Việt

---

## 🎮 Trò chơi có sẵn

1. **Đoán từ (Hangman)** - Đoán chữ cái
2. **Nối đôi (Matching)** - Nối từ với ảnh

---

## 🛠️ Các lệnh hữu ích

```bash
# Thêm dữ liệu mẫu
python seed_data.py

# Tạo tài khoản admin mới
python manage.py createsuperuser

# Xoá tất cả dữ liệu và reset (cẩn thận!)
python manage.py migrate zero lessons
python manage.py migrate

# Kiểm tra lỗi
python manage.py check

# Chạy server trên port khác
python manage.py runserver 8001

# Tạo backup database
copy db.sqlite3 db_backup.sqlite3

# Xem tất cả migrations
python manage.py showmigrations
```

---

## 🌐 URLs chính

| URL                | Mô tả            |
| ------------------ | ---------------- |
| `/`                | Trang chủ        |
| `/register/`       | Đăng ký          |
| `/login/`          | Đăng nhập        |
| `/logout/`         | Đăng xuất        |
| `/lesson/<id>/`    | Chi tiết bài học |
| `/quiz/<id>/`      | Làm bài tập      |
| `/progress/`       | Xem tiến độ      |
| `/badges/`         | Xem huy hiệu     |
| `/games/hangman/`  | Chơi đoán từ     |
| `/games/matching/` | Chơi nối đôi     |
| `/admin/`          | Trang quản trị   |

---

## 🐛 Các lỗi thường gặp & cách sửa

| Lỗi                                             | Giải pháp                                              |
| ----------------------------------------------- | ------------------------------------------------------ |
| "ModuleNotFoundError: No module named 'django'" | `pip install -r requirements.txt`                      |
| "Port 8000 already in use"                      | `python manage.py runserver 8001`                      |
| "Database is locked"                            | Xóa `db.sqlite3`, chạy `python manage.py migrate`      |
| "Image not showing"                             | Kiểm tra thư mục `media/` tồn tại                      |
| "CSS không hiển thị"                            | Cài đặt static files: `python manage.py collectstatic` |

---

## 📁 Cấu trúc tệp quan trọng

```
HocChuCai/
├── manage.py                 # Lệnh quản lý Django
├── db.sqlite3               # Database (tạo tự động)
├── requirements.txt         # Dependencies
├── seed_data.py            # Script thêm dữ liệu
├── README.md               # Tài liệu chính
├── HUONG_DAN.md           # Hướng dẫn chi tiết
├── HocChuCai/
│   ├── settings.py         # Cấu hình
│   ├── urls.py            # Định tuyến chính
│   └── wsgi.py
├── lessons/
│   ├── models.py          # Mô hình dữ liệu
│   ├── views.py           # Logic xử lý
│   ├── urls.py            # Định tuyến app
│   ├── admin.py           # Quản lý admin
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, hình ảnh
```

---

## 💡 Mẹo sử dụng

1. **Học sinh mới**: Bắt đầu với "Đăng ký" trước
2. **Giáo viên**: Đăng nhập admin để thêm bài học
3. **Thêm câu hỏi**: Vào admin → Questions → Add Question
4. **Kiểm tra câu trả lời**: Admin → Quiz Answers
5. **Cấp huy hiệu**: Admin → Badges → Chọn học sinh

---

## 🎯 Quy trình sử dụng toàn bộ

### Cho học sinh:

```
Đăng ký → Đăng nhập → Chọn bài → Xem nội dung → Làm bài tập → Xem kết quả
                                 ↓
                         (Tùy chọn) Chơi trò chơi
                                 ↓
                         Xem tiến độ & Huy hiệu
```

### Cho giáo viên:

```
Đăng nhập admin → Thêm bài học → Thêm câu hỏi → Thêm tùy chọn
                                                     ↓
                              Học sinh làm bài → Kiểm tra kết quả
                                                     ↓
                                        Cấp huy hiệu nếu cần
```

---

## 📞 Cần giúp?

1. **Kiểm tra README.md** - Tài liệu đầy đủ
2. **Kiểm tra HUONG_DAN.md** - Hướng dẫn chi tiết
3. **Xem error trong terminal** - Thường có gợi ý fix
4. **Xem console trình duyệt** - Nhấn F12

---

**Bắt đầu ngay! Happy Learning! 🌟**
