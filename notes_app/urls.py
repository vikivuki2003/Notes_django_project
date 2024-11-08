from django.urls import path

from notes_app.views import RegisterView

urlpatterns = [
    path('register/',RegisterView, name='register'),
    path('login/',LoginView, name='login'),
]