from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    """Bài học tiếng Việt"""
    LESSON_TYPES = [
        ('alphabet', 'Chữ cái'),
        ('vocabulary', 'Từ vựng'),
        ('sentences', 'Câu cơ bản'),
        ('sounds', 'Phát âm'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPES)
    order = models.IntegerField(default=0)
    content = models.TextField()  # HTML content
    image = models.ImageField(upload_to='lessons/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Question(models.Model):
    """Câu hỏi bài tập"""
    QUESTION_TYPES = [
        ('multiple_choice', 'Chọn đáp án'),
        ('text_input', 'Nhập text'),
        ('matching', 'Nối đôi'),
    ]
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    image = models.ImageField(upload_to='questions/', null=True, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.question_text


class QuestionOption(models.Model):
    """Tùy chọn trả lời"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='options/', null=True, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.text


class StudentProgress(models.Model):
    """Theo dõi tiến độ học tập"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.SET_NULL)
    total_score = models.IntegerField(default=0)
    lessons_completed = models.ManyToManyField(Lesson, related_name='completed_by', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Progress"


class QuizAnswer(models.Model):
    """Câu trả lời của học sinh"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(QuestionOption, null=True, blank=True, on_delete=models.SET_NULL)
    text_answer = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.question.question_text}"


class Badge(models.Model):
    """Huy hiệu thành tích"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/')
    condition = models.CharField(max_length=200)  # Điều kiện để có được huy hiệu
    users = models.ManyToManyField(User, related_name='badges', blank=True)
    
    def __str__(self):
        return self.name
