# 🔊 HƯỚNG DẪN TÍNH NĂNG ÂM THANH VÀ PHÔNG CHỮ

## 📋 Tổng quan cập nhật

Ứng dụng đã được nâng cấp với:
- ✅ **Hệ thống âm thanh** - Phát âm chữ cái bằng Web Speech API
- ✅ **Phông chữ mới** - Montserrat & Nunito cho giao diện đẹp hơn
- ✅ **Template chuyên biệt** - Trang chữ cái tương tác

---

## 🔊 TÍNH NĂNG ÂM THANH

### 1. Phát âm chữ cái

**Ở trang bài học chữ cái:**

#### Cách sử dụng:
1. Vào bài học chữ cái
2. **Nhấp vào mỗi chữ** hoặc **nút 🔊 Phát âm** để nghe cách phát âm
3. Lặp lại theo âm thanh để luyện tập

#### Ví dụ:
```
┌─────────────────┐
│        A        │  ← Nhấp vào để nghe "A"
│     Chữ A       │
│       🔊        │
└─────────────────┘
```

### 2. Phát âm tiêu đề bài học

**Trên header bài học:**
- Nút 🔊 ở bên cạnh tiêu đề
- Nhấp để nghe cách phát âm tiêu đề bài học

### 3. Hướng dẫn phát âm chi tiết

**Dưới cùng mỗi trang chữ cái:**
- Bảng hướng dẫn phát âm chi tiết
- Ví dụ từ vựng sử dụng chữ đó
- Nút 🔊 để nghe từng chữ

---

## 🎨 CẬP NHẬT PHÔNG CHỮ

### Phông chữ mới dùng

| Phông chữ | Sử dụng | Tính năng |
|-----------|--------|----------|
| **Montserrat** | Tiêu đề, heading | Đậm, rõ ràng, thích hợp cho trẻ em |
| **Nunito** | Nội dung, text | Mềm mại, dễ đọc, thân thiện |

### Cải thiện giao diện

- ✅ **Tiêu đề sắc nét hơn** - Font Montserrat 700-800 weight
- ✅ **Văn bản dễ đọc hơn** - Font Nunito với line-height 1.6
- ✅ **Khoảng cách chữ tốt hơn** - Letter-spacing 0.3px
- ✅ **Bắt mắt hơn** - Các heading bây giờ nổi bật rõ ràng

### So sánh:
```
TRƯỚC:                    SAU:
Comic Sans MS          →  Montserrat + Nunito
Generic Font           →  Professional Font
Khó đọc trên mobile    →  Rõ ràng trên mọi thiết bị
```

---

## 📱 TÍCH HỢP ÂMTHANH

### Công nghệ dùng

**Web Speech API** (có sẵn trong trình duyệt)
- Tự động phát âm tiếng Việt
- Không cần file âm thanh bổ sung
- Hoạt động online

### Các trình duyệt hỗ trợ

| Trình duyệt | Hỗ trợ |
|-------------|--------|
| Chrome / Edge | ✅ Đầy đủ |
| Firefox | ✅ Đầy đủ |
| Safari | ✅ Hỗ trợ cơ bản |
| Internet Explorer | ❌ Không hỗ trợ |

### Cấu hình âm thanh

File: `lessons/static/js/audio.js`

```javascript
// Tốc độ phát âm (0.5 = chậm, 1 = bình thường, 2 = nhanh)
utterance.rate = 0.8;

// Tông giọng (0.5 - 2, mặc định 1)
utterance.pitch = 1;

// Âm lượng (0 - 1)
utterance.volume = 1;
```

#### Chỉnh lại tốc độ:
1. Mở file: `lessons/static/js/audio.js`
2. Tìm dòng: `utterance.rate = 0.8`
3. Đổi thành:
   - `0.5` - Phát âm chậm (cho bé nhỏ)
   - `0.8` - Phát âm bình thường (mặc định)
   - `1.2` - Phát âm nhanh

---

## 📝 CÁCH DÙNG CỦA TRẺ EM

### Học chữ cái từng bước

**Bước 1: Vào bài học**
```
Trang chủ → Chọn "Chữ A, Â, Ă" → Vào bài học
```

**Bước 2: Nghe phát âm**
```
Nhấp vào từng chữ (A, Â, Ă) → Nghe âm thanh
```

**Bước 3: Lặp lại**
```
Nhấp nhiều lần → Nhớ âm thanh → Lặp lại theo
```

**Bước 4: Đọc ví dụ**
```
Xem "Hướng dẫn phát âm chi tiết" dưới cùng
Nghe từ ví dụ (ăn, ân cần, ặc, v.v.)
```

**Bước 5: Làm bài tập**
```
Nút "Làm bài tập →" → Trả lời câu hỏi
```

---

## 👨‍🏫 HƯỚNG DẪN CHO GIÁO VIÊN

### Chuẩn bị lớp học

1. **Kiểm tra âm thanh trước**
   - Mở trang chữ cái
   - Test phát âm trên máy tính của mình
   - Kết nối loa để trẻ em nghe được

2. **Huấn luyện cách dùng**
   - Cho trẻ em xem cách nhấp vào chữ
   - Nhân mạnh: "Nghe rồi lặp lại"
   - Khích lệ trẻ phát âm cùng

3. **Hoạt động nhóm**
   - Chia trẻ em thành nhóm
   - Mỗi nhóm chọn một chữ
   - Nghe và lặp lại cùng nhau

### Bài tập lớp học

#### Bài tập 1: Nghe và chỉ
```
1. Phát âm chữ "A"
2. Trẻ em nghe
3. Trẻ em chỉ vào chữ "A"
4. Nhận phần thưởng (huy hiệu)
```

#### Bài tập 2: Nghe và viết
```
1. Phát âm chữ
2. Trẻ em không nhìn thấy chữ
3. Trẻ em viết chữ gì
4. Kiểm tra trên web
```

#### Bài tập 3: Điền ví dụ từ
```
Phát âm: "Chữ A, ví dụ: ăn cơm"
Trẻ em tìm từ khác với chữ "A"
Ghi lại kết quả
```

---

## 🐛 GIẢI QUYẾT VẤN ĐỀ ÂM THANH

### Vấn đề 1: Không nghe được âm thanh

**Nguyên nhân có thể:**
1. Trình duyệt không hỗ trợ (IE)
2. Âm lượng máy tính tắt
3. Trình duyệt tắt âm thanh trang web

**Giải pháp:**
```
1. Dùng Chrome, Firefox, Edge, Safari
2. Kiểm tra âm lượng Windows / Mac
3. Bấm nút volume ở góc trình duyệt
4. Bật microphone (nếu được hỏi)
5. F5 reload trang
```

### Vấn đề 2: Âm thanh quá nhanh / quá chậm

**Giải pháp:**
1. Mở file: `lessons/static/js/audio.js`
2. Tìm dòng `utterance.rate = 0.8`
3. Đổi:
   - Quá nhanh → Giảm thành `0.6`
   - Quá chậm → Tăng thành `1.0`
4. Save file
5. Reload trang web (F5)

### Vấn đề 3: Giọng không phải tiếng Việt

**Giải pháp:**
1. Đây là vấn đề của hệ điều hành
2. Windows:
   ```
   Cài đặt → Thời gian & ngôn ngữ → Ngôn ngữ
   → Tìm "Tiếng Việt" → Cài đặt bộ TTS
   ```
3. macOS:
   ```
   System Preferences → Accessibility → Speech
   → Chọn "Tuyên bố ứng dụng"
   → Chọn "Tiếng Việt" (nếu có)
   ```

---

## 🎯 TÍNH NĂNG NÂNG CAO

### Tùy chỉnh âm thanh bằng code

**File:** `lessons/static/js/audio.js`

```javascript
// Phát âm một từ
speak("Chữ A");

// Phát âm với tốc độ tùy chỉnh
speak("Chữ A", 0.5);  // Chậm
speak("Chữ A", 1.2);  // Nhanh

// Dừng phát âm
stopSpeech();
```

### Thêm âm thanh vào trang khác

**HTML:**
```html
<!-- Nút phát âm -->
<button data-audio-btn data-audio-text="Chữ A">🔊 Phát âm</button>

<!-- Hoặc nhấp để nghe -->
<div data-pronounce data-audio-text="Chữ A">A</div>
```

**JavaScript:**
```javascript
// Trong các template khác
<script src="{% static 'js/audio.js' %}"></script>
```

---

## 📊 THỐNG KÊ SỬ DỤNG

### Tracking

Hệ thống hiện chưa track số lần phát âm, nhưng có thể thêm bằng cách:

```python
# Trong models.py
class AudioPlayLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.CharField(max_length=10)
    played_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
```

---

## 🔔 THÔNG BÁO CHUẨN BỊ

### Cải thiện sắp tới

- [ ] Thêm file âm thanh mp3 tùy chỉnh
- [ ] Lưu số lần phát âm của mỗi học sinh
- [ ] Thêm micro để ghi âm học sinh
- [ ] So sánh phát âm của bé với mẫu
- [ ] Thêm huy hiệu "Phát âm tốt"

---

## 📞 HỖ TRỢ

### Nếu gặp vấn đề:

1. **Kiểm tra console** (F12 → Console)
2. **Xem logs server**:
   ```powershell
   # Terminal đang chạy Django
   # Xem tin nhắn lỗi
   ```
3. **Đọc README.md** để biết cách setup
4. **Thử browser khác** để xác nhận vấn đề

---

## ✅ CHECKLIST HOÀN THÀNH

- [x] Thêm Web Speech API
- [x] Phát âm chữ cái
- [x] Cập nhật phông chữ
- [x] Template chuyên biệt cho chữ cái
- [x] Hướng dẫn phát âm chi tiết
- [x] Tài liệu này

---

**Made with ❤️ for Vietnamese Education**

Happy Learning! 🎉
