from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from notes_app import views
from notes_app.views import RegisterView, CreateView, NoteDetailView, NoteCreateView, NoteUpdateView, note_delete_view, \
    MainPageView

app_name = 'notes_app'
urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('create', NoteCreateView.as_view(), name='create'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',auth_views.LoginView.as_view(next_page='notes_app:main'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='notes_app:main'), name='logout'),
    path('notes_list/', views.note_list_view, name='notes_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note/<int:pk>/delete/', note_delete_view, name='note_delete'),
    path('note_update/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),

]