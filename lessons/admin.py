from django.contrib import admin
from .models import Lesson, Question, QuestionOption, StudentProgress, QuizAnswer, Badge

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson_type', 'order']
    list_filter = ['lesson_type']
    search_fields = ['title', 'description']
    ordering = ['order']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'lesson', 'question_type', 'order']
    list_filter = ['lesson', 'question_type']
    search_fields = ['question_text']

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['text']

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_score', 'current_lesson']
    list_filter = ['created_at']
    search_fields = ['user__username']

@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'is_correct', 'answered_at']
    list_filter = ['is_correct', 'answered_at']
    search_fields = ['user__username']

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'condition']
    search_fields = ['name']
