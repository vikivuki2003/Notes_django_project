from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from notes_app import views
from notes_app.views import RegisterView, HomeView, NoteDetailView, NoteCreateView, NoteUpdateView, note_delete_view

app_name = 'notes_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(next_page='home'), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note_create', NoteCreateView.as_view(), name='note_create'),
    path('note/<int:pk>/delete/', note_delete_view, name='note_delete'),
    path('note_update/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),

]