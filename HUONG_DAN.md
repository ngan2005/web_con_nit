# 📚 Hướng dẫn sử dụng HỌC CHỮ CÁI

## 🎯 Giới thiệu

**Học Chữ Cái** là một ứng dụng web được thiết kế để giúp trẻ em học tiếng Việt một cách vui vẻ, hiệu quả và tương tác. Ứng dụng này được xây dựng bằng **Django** (Python) và có giao diện thân thiện với trẻ em.

## 🚀 Bắt đầu nhanh

### 1. Chuẩn bị môi trường

```bash
# Di chuyển vào thư mục dự án
cd D:\pythonweb

# Kích hoạt virtual environment
.venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy migration (nếu lần đầu)
python manage.py migrate

# Chạy server
python manage.py runserver
```

### 2. Truy cập ứng dụng

- **Trang chủ**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

## 📖 Hướng dẫn cho học sinh

### ✍️ Đăng ký tài khoản

1. Vào trang chủ
2. Bấm nút **"Đăng ký"** (góc phải trên)
3. Điền thông tin:
   - **Tên đăng nhập**: Chọn tên bạn thích (không có dấu cách, không có ký tự đặc biệt)
   - **Email**: Địa chỉ email của bạn
   - **Mật khẩu**: Chọn mật khẩu an toàn
   - **Xác nhận mật khẩu**: Nhập lại mật khẩu
4. Bấm **"Đăng ký"** → Bạn sẽ tự động được đăng nhập

### 🔑 Đăng nhập

1. Bấm **"Đăng nhập"** ở trang chủ
2. Nhập tên đăng nhập và mật khẩu
3. Bấm **"Đăng nhập"**

### 📚 Học bài

1. **Xem danh sách bài học** ở trang chủ
2. **Bấm vào bài học** để xem chi tiết:
   - 📖 Nội dung bài học
   - 🖼️ Hình ảnh minh họa
   - 📝 Mô tả chi tiết
3. **Bấm "Làm bài tập"** để kiểm tra kiến thức

### ✅ Làm bài tập

1. Đọc câu hỏi cẩn thận
2. Bấm vào đáp án bạn cho là đúng
3. Tiếp tục cho đến hết câu hỏi
4. Bấm **"Nộp bài"** để kiểm tra kết quả

### 📊 Xem kết quả

Sau khi nộp bài, bạn sẽ thấy:

- ✔️ Số câu đúng / Tổng số câu
- 📈 Phần trăm hoàn thành
- ⭐ Số sao (dựa trên điểm)
- 💡 Gợi ý để cải thiện

### 🎮 Chơi trò chơi

#### 🎪 Trò chơi Đoán từ (Hangman)

- Đoán chữ cái từng cái một
- Có 6 lượt đoán sai
- Cố gắng đoán đúng từ trước khi hết lượt

Cách chơi:

1. Bấm các nút chữ cái
2. Nếu đúng, chữ cái sẽ hiện ra
3. Nếu sai, bạn mất một lượt
4. Hoàn thành từ trước khi nhân vật chết!

#### 🔗 Trò chơi Nối đôi (Matching)

- Nối từ tiếng Việt với ảnh hoặc định nghĩa
- Nhanh chóng và vui nhộn

Cách chơi:

1. Bấm vào một từ ở bên trái
2. Bấm vào ảnh/định nghĩa tương ứng ở bên phải
3. Nối tất cả các cặp để chiến thắng

### 📊 Theo dõi tiến độ

1. Bấm **"Tiến độ"** ở menu trên
2. Xem:
   - 📈 Phần trăm bài học hoàn thành
   - 📚 Số bài học đã làm
   - 🏆 Tổng điểm đạt được
   - ✅ Trạng thái của từng bài

### 🏆 Huy hiệu

1. Bấm **"Huy hiệu"** ở menu trên
2. Xem các huy hiệu bạn đã đạt
3. Các huy hiệu khóa sẽ mở khi bạn hoàn thành điều kiện

### 🚪 Đăng xuất

1. Bấm tên của bạn ở góc phải trên
2. Bấm **"Đăng xuất"** để thoát

---

## 👨‍💼 Hướng dẫn cho giáo viên / Quản trị viên

### 🔐 Truy cập trang quản trị

1. Vào: http://127.0.0.1:8000/admin/
2. Đăng nhập bằng tài khoản admin
3. Bạn sẽ thấy bảng điều khiển quản lý

### 📚 Quản lý bài học

#### Thêm bài học mới

1. Bấm **"Lessons"** → **"Add Lesson"**
2. Điền thông tin:
   - **Title**: Tên bài học (VD: "Chữ A, Â, Ă")
   - **Description**: Mô tả ngắn
   - **Lesson type**: Chọn loại:
     - 🔤 Chữ cái
     - 📖 Từ vựng
     - 💬 Câu cơ bản
     - 🎵 Phát âm
   - **Order**: Thứ tự bài học (1, 2, 3, ...)
   - **Content**: Nội dung HTML (có thể tạo bài học đẹp với HTML)
   - **Image**: Hình ảnh bài học (tùy chọn)
   - **Audio**: File âm thanh (tùy chọn)
3. Bấm **"Save"**

#### Chỉnh sửa bài học

1. Tìm bài học trong danh sách
2. Bấm vào tiêu đề bài học
3. Sửa thông tin cần thiết
4. Bấm **"Save"**

#### Xóa bài học

1. Tìm bài học
2. Chọn checkbox bên cạnh bài học
3. Chọn "Delete selected lessons" từ dropdown trên
4. Bấm "Go"

### ❓ Quản lý câu hỏi

#### Thêm câu hỏi

1. Bấm **"Questions"** → **"Add Question"**
2. Điền thông tin:
   - **Lesson**: Chọn bài học chứa câu hỏi
   - **Question text**: Nội dung câu hỏi
   - **Question type**: Chọn loại câu hỏi:
     - 🎯 Multiple choice (chọn đáp án)
     - 📝 Text input (nhập text)
     - 🔗 Matching (nối đôi)
   - **Order**: Thứ tự câu hỏi
   - **Image**: Hình ảnh câu hỏi (tùy chọn)
3. Bấm **"Save and add another"** để tiếp tục thêm

#### Thêm tùy chọn trả lời

1. Trong trang câu hỏi, kéo xuống phần "Question options"
2. Bấm **"Add another Question option"**
3. Điền:
   - **Text**: Nội dung tùy chọn
   - **Is correct**: Đánh dấu nếu đây là đáp án đúng
   - **Image**: Hình ảnh tùy chọn (tùy chọn)
4. Lặp lại cho tất cả các tùy chọn

### 👥 Quản lý học sinh

#### Xem thông tin học sinh

1. Bấm **"Student Progresses"**
2. Xem danh sách học sinh

#### Xem tiến độ của từng học sinh

1. Bấm vào tên học sinh
2. Xem:
   - Bài học hiện tại
   - Tổng điểm
   - Bài học đã hoàn thành
   - Huy hiệu

#### Xem câu trả lời

1. Bấm **"Quiz Answers"**
2. Lọc theo học sinh hoặc câu hỏi
3. Xem chi tiết từng câu trả lời

### 🏆 Quản lý huy hiệu

#### Thêm huy hiệu mới

1. Bấm **"Badges"** → **"Add Badge"**
2. Điền:
   - **Name**: Tên huy hiệu (VD: "Thiên tài")
   - **Description**: Mô tả huy hiệu
   - **Icon**: Hình ảnh huy hiệu
   - **Condition**: Điều kiện để đạt huy hiệu
3. Bấm **"Save"**

#### Cấp huy hiệu cho học sinh

1. Bấm vào huy hiệu
2. Ở phần "Users", tìm và chọn học sinh
3. Bấm **"Save"**

---

## 💡 Lời khuyên sử dụng

### Cho học sinh

- 🎯 **Học thường xuyên**: Mỗi ngày 15-30 phút
- 📖 **Đọc kỹ nội dung** trước khi làm bài
- 🎮 **Chơi trò chơi** để luyện tập thêm
- 📊 **Theo dõi tiến độ** để có động lực
- 🏆 **Cố gắng đạt huy hiệu** để phát triển

### Cho giáo viên

- 📚 **Tạo bài học theo chủ đề**: Sắp xếp logic
- ❓ **Thêm câu hỏi đa dạng**: Nhiều hình thức
- 🎮 **Khuyến khích chơi trò chơi**: Vừa vui vừa học
- 📊 **Kiểm tra tiến độ** thường xuyên
- 🏆 **Trao huy hiệu** để tạo động lực

---

## 🆘 Giải quyết vấn đề

### Lỗi: Server không khởi động

**Giải pháp:**

```bash
# 1. Kiểm tra Python
python --version

# 2. Kiểm tra Django
python -m django --version

# 3. Kiểm tra migrations
python manage.py migrate

# 4. Thử port khác
python manage.py runserver 8001
```

### Lỗi: Database bị khóa

**Giải pháp:**

```bash
# Xóa file db.sqlite3 (nếu có dữ liệu backup)
# Rồi chạy lại
python manage.py migrate
python seed_data.py
```

### Lỗi: Quên mật khẩu admin

**Giải pháp:**

```bash
# Tạo admin mới
python manage.py createsuperuser
```

### Trang không hiển thị CSS/hình ảnh

**Giải pháp:**

```bash
# Collect static files
python manage.py collectstatic --noinput
```

### Hình ảnh không tải lên

**Giải pháp:**

1. Kiểm tra thư mục `media/` có tồn tại không
2. Kiểm tra quyền truy cập thư mục
3. Kiểm tra file `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 📱 Tính năng nâng cao

### Tự động cấp huy hiệu

Bạn có thể tạo script để tự động cấp huy hiệu:

```python
from lessons.models import Badge, StudentProgress

def award_badges():
    for progress in StudentProgress.objects.all():
        # Hoàn thành 5 bài
        if progress.lessons_completed.count() >= 5:
            badge = Badge.objects.get(name="Starter")
            progress.user.badges.add(badge)

        # Điểm > 100
        if progress.total_score >= 100:
            badge = Badge.objects.get(name="Champion")
            progress.user.badges.add(badge)
```

### Xuất báo cáo

```python
from django.db.models import Count

# Điểm cao nhất
top_students = StudentProgress.objects.order_by('-total_score')[:10]

# Bài học được yêu thích nhất
popular_lessons = Lesson.objects.annotate(
    num_completed=Count('completed_by')
).order_by('-num_completed')
```

---

## 🎨 Tùy chỉnh giao diện

### Thay đổi màu sắc

Sửa trong `base.html`:

```css
/* Thay đổi màu chính */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Thành */
background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
```

### Thay đổi font

Sửa trong `base.html`:

```css
font-family: "Comic Sans MS", "Segoe UI", ...;

/* Thành */
font-family: "Arial", "Helvetica", ...;
```

### Thêm logo

Sửa HTML:

```html
<div class="logo">
  <em>🎓</em>
  <!-- Đổi emoji -->
  <img src="logo.png" />
  <!-- Hoặc thêm ảnh -->
</div>
```

---

## 📞 Liên hệ hỗ trợ

Nếu gặp vấn đề:

1. Kiểm tra file `README.md`
2. Kiểm tra error log
3. Xem thử trong browser console (F12)

---

## 🎯 Bước tiếp theo

Để phát triển ứng dụng thêm:

- [ ] Thêm phần phát âm audio
- [ ] Tích hợp text-to-speech
- [ ] Tạo mobile app
- [ ] Thêm hệ thống thi cuối kỳ
- [ ] Xuất chứng chỉ
- [ ] Tích hợp payment (nếu cần)

---

**Chúc bạn có một trải nghiệm tuyệt vời!** 🌟

Được tạo với ❤️ cho giáo dục tiếng Việt
