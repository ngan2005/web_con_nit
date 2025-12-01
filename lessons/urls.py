from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('quiz/<int:lesson_id>/', views.quiz, name='quiz'),
    path('quiz/<int:lesson_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('progress/', views.progress, name='progress'),
    path('badges/', views.my_badges, name='badges'),
    path('games/hangman/', views.game_hangman, name='game_hangman'),
    path('games/matching/', views.game_matching, name='game_matching'),
]
