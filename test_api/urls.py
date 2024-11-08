from django.urls import path

from test_api.views import NoteDetail, NoteList

app_name = 'api'

urlpatterns = [
    path('<int:pk>/', NoteDetail.as_view(), name='note_detail'),
    path("", NoteList.as_view(), name="note_list"),
]