"""
File kiểm tra ứng dụng Học Chữ Cái
Chạy: python manage.py test
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from lessons.models import Lesson, Question, QuestionOption, StudentProgress


class LessonTestCase(TestCase):
    """Kiểm tra các bài học"""
    
    def setUp(self):
        """Chuẩn bị dữ liệu test"""
        self.lesson = Lesson.objects.create(
            title='Test Lesson',
            description='Test Description',
            lesson_type='alphabet',
            order=1,
            content='<h1>Test</h1>'
        )
    
    def test_lesson_creation(self):
        """Kiểm tra tạo bài học"""
        self.assertEqual(self.lesson.title, 'Test Lesson')
        self.assertEqual(self.lesson.lesson_type, 'alphabet')
    
    def test_lesson_str(self):
        """Kiểm tra hiển thị bài học"""
        self.assertEqual(str(self.lesson), 'Test Lesson')


class QuestionTestCase(TestCase):
    """Kiểm tra câu hỏi"""
    
    def setUp(self):
        """Chuẩn bị dữ liệu test"""
        self.lesson = Lesson.objects.create(
            title='Test Lesson',
            description='Test',
            lesson_type='alphabet',
            order=1,
            content='Test'
        )
        
        self.question = Question.objects.create(
            lesson=self.lesson,
            question_text='What is 1+1?',
            question_type='multiple_choice',
            order=1
        )
        
        self.option1 = QuestionOption.objects.create(
            question=self.question,
            text='2',
            is_correct=True,
            order=1
        )
        
        self.option2 = QuestionOption.objects.create(
            question=self.question,
            text='3',
            is_correct=False,
            order=2
        )
    
    def test_question_creation(self):
        """Kiểm tra tạo câu hỏi"""
        self.assertEqual(self.question.question_text, 'What is 1+1?')
        self.assertEqual(self.question.lesson, self.lesson)
    
    def test_question_options(self):
        """Kiểm tra các tùy chọn"""
        self.assertEqual(self.question.options.count(), 2)
        correct_option = self.question.options.filter(is_correct=True).first()
        self.assertEqual(correct_option.text, '2')


class StudentProgressTestCase(TestCase):
    """Kiểm tra theo dõi tiến độ học sinh"""
    
    def setUp(self):
        """Chuẩn bị dữ liệu test"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.progress = StudentProgress.objects.create(user=self.user)
        self.lesson = Lesson.objects.create(
            title='Test Lesson',
            description='Test',
            lesson_type='alphabet',
            order=1,
            content='Test'
        )
    
    def test_progress_creation(self):
        """Kiểm tra tạo tiến độ"""
        self.assertEqual(self.progress.user, self.user)
        self.assertEqual(self.progress.total_score, 0)
    
    def test_add_completed_lesson(self):
        """Kiểm tra thêm bài học hoàn thành"""
        self.progress.lessons_completed.add(self.lesson)
        self.assertEqual(self.progress.lessons_completed.count(), 1)
