from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from .models import (
    Lesson, Question, QuestionOption, StudentProgress, 
    QuizAnswer, Badge
)


def home(request):
    """Trang chủ"""
    lessons = Lesson.objects.all().order_by('order')
    if request.user.is_authenticated:
        progress = StudentProgress.objects.get_or_create(user=request.user)[0]
        return render(request, 'lessons/home.html', {
            'lessons': lessons,
            'progress': progress,
        })
    return render(request, 'lessons/home.html', {'lessons': lessons})


def register(request):
    """Đăng ký tài khoản"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            return render(request, 'lessons/register.html', 
                        {'error': 'Mật khẩu không khớp'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'lessons/register.html', 
                        {'error': 'Tên đăng nhập đã tồn tại'})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        StudentProgress.objects.create(user=user)
        
        # Đăng nhập tự động
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'lessons/register.html')


def login_view(request):
    """Đăng nhập"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'lessons/login.html',
                        {'error': 'Tên đăng nhập hoặc mật khẩu không đúng'})
    
    return render(request, 'lessons/login.html')


def logout_view(request):
    """Đăng xuất"""
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def lesson_detail(request, lesson_id):
    """Xem chi tiết bài học"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress = StudentProgress.objects.get_or_create(user=request.user)[0]
    
    context = {
        'lesson': lesson,
        'progress': progress,
        'is_completed': lesson in progress.lessons_completed.all(),
    }
    
    return render(request, 'lessons/lesson_detail.html', context)


@login_required(login_url='login')
def quiz(request, lesson_id):
    """Làm bài tập"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = lesson.questions.all()
    
    context = {
        'lesson': lesson,
        'questions': questions,
    }
    
    return render(request, 'lessons/quiz.html', context)


@login_required(login_url='login')
@require_POST
def submit_quiz(request, lesson_id):
    """Nộp bài quiz"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = lesson.questions.all()
    
    score = 0
    total = questions.count()
    
    for question in questions:
        if question.question_type == 'multiple_choice':
            option_id = request.POST.get(f'question_{question.id}')
            if option_id:
                option = get_object_or_404(QuestionOption, id=option_id)
                is_correct = option.is_correct
                if is_correct:
                    score += 1
                QuizAnswer.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=option,
                    is_correct=is_correct
                )
    
    # Cập nhật tiến độ
    progress = StudentProgress.objects.get_or_create(user=request.user)[0]
    progress.lessons_completed.add(lesson)
    progress.total_score += score
    progress.save()
    
    percentage = (score / total * 100) if total > 0 else 0
    
    return render(request, 'lessons/quiz_result.html', {
        'lesson': lesson,
        'score': score,
        'total': total,
        'percentage': percentage,
    })


@login_required(login_url='login')
def progress(request):
    """Xem tiến độ"""
    progress = StudentProgress.objects.get_or_create(user=request.user)[0]
    completed_lessons = progress.lessons_completed.all()
    all_lessons = Lesson.objects.all()
    total_lessons = all_lessons.count()
    completion_percentage = (completed_lessons.count() / total_lessons * 100) if total_lessons > 0 else 0
    
    context = {
        'progress': progress,
        'completed_lessons': completed_lessons,
        'lessons': all_lessons,
        'total_lessons': total_lessons,
        'completion_percentage': completion_percentage,
    }
    
    return render(request, 'lessons/progress.html', context)


@login_required(login_url='login')
def my_badges(request):
    """Xem huy hiệu"""
    badges = request.user.badges.all()
    
    return render(request, 'lessons/badges.html', {
        'badges': badges,
    })


def game_hangman(request):
    """Trò chơi đoán từ"""
    return render(request, 'lessons/games/hangman.html')


def game_matching(request):
    """Trò chơi nối đôi"""
    return render(request, 'lessons/games/matching.html')
