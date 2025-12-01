import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HocChuCai.settings')
django.setup()

from lessons.models import Lesson, Question, QuestionOption

# Xóa dữ liệu cũ
Lesson.objects.all().delete()

# Tạo bài học về chữ cái
lesson1 = Lesson.objects.create(
    title='Chữ A, Â, Ă',
    description='Học các chữ cái đầu tiên: A, Â, Ă',
    lesson_type='alphabet',
    order=1,
    content='''
    <h2>🔤 Các chữ cái A, Â, Ă</h2>
    <p>Dưới đây là các chữ cái bắt đầu bằng "A":</p>
    <p><strong>A:</strong> Chữ cái thứ nhất trong bảng chữ cái tiếng Việt</p>
    <p><strong>Â:</strong> Một biến thể của chữ A (phát âm khác)</p>
    <p><strong>Ă:</strong> Một biến thể khác của chữ A</p>
    <p style="font-size: 32px; margin: 20px 0;">A &nbsp;&nbsp;&nbsp; Â &nbsp;&nbsp;&nbsp; Ă</p>
    <p>Hãy luyện tập phát âm các chữ này nhiều lần!</p>
    '''
)

# Tạo các câu hỏi cho bài học 1
q1 = Question.objects.create(
    lesson=lesson1,
    question_text='Chữ A được phát âm như thế nào?',
    question_type='multiple_choice',
    order=1
)
QuestionOption.objects.create(question=q1, text='Aaaa (dài)', is_correct=True, order=1)
QuestionOption.objects.create(question=q1, text='Ơơơ (ngắn)', is_correct=False, order=2)
QuestionOption.objects.create(question=q1, text='Ưưư (mũi)', is_correct=False, order=3)

q2 = Question.objects.create(
    lesson=lesson1,
    question_text='Chữ Â được dùng trong từ nào?',
    question_type='multiple_choice',
    order=2
)
QuestionOption.objects.create(question=q2, text='Mâu', is_correct=False, order=1)
QuestionOption.objects.create(question=q2, text='Âm', is_correct=True, order=2)
QuestionOption.objects.create(question=q2, text='Ám', is_correct=False, order=3)

# Tạo bài học về từ vựng
lesson2 = Lesson.objects.create(
    title='Từ vựng: Động vật',
    description='Học các từ vựng về động vật',
    lesson_type='vocabulary',
    order=2,
    content='''
    <h2>📖 Các động vật</h2>
    <p>Dưới đây là các từ vựng về động vật:</p>
    <p><strong>Con Mèo:</strong> 🐱 Một con vật nuôi</p>
    <p><strong>Con Chó:</strong> 🐶 Bạn thân thiết</p>
    <p><strong>Con Chim:</strong> 🐦 Có cánh và lông</p>
    <p><strong>Con Cá:</strong> 🐟 Sống dưới nước</p>
    '''
)

q3 = Question.objects.create(
    lesson=lesson2,
    question_text='Con mèo tiếng Việt là gì?',
    question_type='multiple_choice',
    order=1
)
QuestionOption.objects.create(question=q3, text='Meo', is_correct=False, order=1)
QuestionOption.objects.create(question=q3, text='Mèo', is_correct=True, order=2)
QuestionOption.objects.create(question=q3, text='Meow', is_correct=False, order=3)

q4 = Question.objects.create(
    lesson=lesson2,
    question_text='Con chó tiếng Việt là gì?',
    question_type='multiple_choice',
    order=2
)
QuestionOption.objects.create(question=q4, text='Chó', is_correct=True, order=1)
QuestionOption.objects.create(question=q4, text='Chó mèo', is_correct=False, order=2)
QuestionOption.objects.create(question=q4, text='Woof', is_correct=False, order=3)

# Tạo bài học về câu cơ bản
lesson3 = Lesson.objects.create(
    title='Câu cơ bản: Giới thiệu',
    description='Học các câu giới thiệu cơ bản',
    lesson_type='sentences',
    order=3,
    content='''
    <h2>💬 Các câu giới thiệu cơ bản</h2>
    <p><strong>Xin chào!</strong> - Lời chào</p>
    <p><strong>Tôi tên là...</strong> - Giới thiệu tên</p>
    <p><strong>Bạn tên là gì?</strong> - Hỏi tên</p>
    <p><strong>Cảm ơn!</strong> - Cảm ơn</p>
    <p><strong>Tạm biệt!</strong> - Lời chia tay</p>
    '''
)

q5 = Question.objects.create(
    lesson=lesson3,
    question_text='Cách nói "hello" trong tiếng Việt là?',
    question_type='multiple_choice',
    order=1
)
QuestionOption.objects.create(question=q5, text='Xin chào', is_correct=True, order=1)
QuestionOption.objects.create(question=q5, text='Cảm ơn', is_correct=False, order=2)
QuestionOption.objects.create(question=q5, text='Tạm biệt', is_correct=False, order=3)

q6 = Question.objects.create(
    lesson=lesson3,
    question_text='Cách nói "thank you" trong tiếng Việt là?',
    question_type='multiple_choice',
    order=2
)
QuestionOption.objects.create(question=q6, text='Xin chào', is_correct=False, order=1)
QuestionOption.objects.create(question=q6, text='Cảm ơn', is_correct=True, order=2)
QuestionOption.objects.create(question=q6, text='Không', is_correct=False, order=3)

# Tạo bài học về phát âm
lesson4 = Lesson.objects.create(
    title='Phát âm: Nguyên âm cơ bản',
    description='Luyện tập phát âm các nguyên âm',
    lesson_type='sounds',
    order=4,
    content='''
    <h2>🎵 Các nguyên âm cơ bản</h2>
    <p>Nghe và luyện tập phát âm các nguyên âm:</p>
    <p><strong>A:</strong> /a/ - âm "a" bình thường</p>
    <p><strong>E:</strong> /ɛ/ - âm "e" mở</p>
    <p><strong>I:</strong> /i/ - âm "i" ngắn</p>
    <p><strong>O:</strong> /ɔ/ - âm "o" mở</p>
    <p><strong>U:</strong> /u/ - âm "u" dài</p>
    '''
)

q7 = Question.objects.create(
    lesson=lesson4,
    question_text='Nguyên âm nào được phát âm như /a/?',
    question_type='multiple_choice',
    order=1
)
QuestionOption.objects.create(question=q7, text='A', is_correct=True, order=1)
QuestionOption.objects.create(question=q7, text='E', is_correct=False, order=2)
QuestionOption.objects.create(question=q7, text='O', is_correct=False, order=3)

print("✅ Đã thêm dữ liệu mẫu thành công!")
print("📚 Đã tạo 4 bài học:")
print("1. Chữ A, Â, Ă")
print("2. Từ vựng: Động vật")
print("3. Câu cơ bản: Giới thiệu")
print("4. Phát âm: Nguyên âm cơ bản")
