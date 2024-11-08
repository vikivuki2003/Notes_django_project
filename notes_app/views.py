from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, NoteForm
from .models import Note

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class NotesListView(ListView):
    model = Note
    template_name = 'notes_app/note_list.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes_app/note_detail'

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/note_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/note_form.html'

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes_app/delete.html'
    success_url = reverse_lazy('note_list')
