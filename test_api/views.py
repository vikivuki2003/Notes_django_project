from rest_framework import generics
from .serializers import NoteSerializer
from notes_app.models import Notes



class NoteList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer