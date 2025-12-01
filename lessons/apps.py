from django.apps import AppConfig


class LessonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lessons'
    verbose_name = 'Bài Học Tiếng Việt'
    
    def ready(self):
        """Khởi tạo khi app sẵn sàng"""
        pass
