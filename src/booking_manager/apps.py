from django.apps import AppConfig


class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_manager'
    verbose_name = 'Управление бронированиями'  # <-- название раздела
