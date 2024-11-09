from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    messages.success(request, f'Добро пожаловать, {user.username}! Вы успешно вошли в систему.')

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    messages.info(request, 'Вы вышли из системы.')