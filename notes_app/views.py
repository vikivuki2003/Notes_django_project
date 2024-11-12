from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, NotesForm
from .models import Notes


def contact_view(request):
    return render(request, 'notes_app/contact.html')


class MainPageView(ListView):
    model = Notes
    template_name = 'notes_app/main.html'
    context_object_name = 'notes'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('notes_app:login')


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes_app/note_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

class NoteCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes_app/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()  # Сохраняем заметку
        messages.success(self.request, 'Заметка успешно создана!')
        return self.render_to_response({'form': NotesForm()})  # Возвращаем ту же страницу с сообщением

class NoteUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes_app/note_update.html'
    success_url = reverse_lazy('notes_app:main')

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = self.object
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Заметка успешно обновлена!')
        return super().form_valid(form)


def note_delete_view(request, pk):
    note = get_object_or_404(Notes.objects.filter(user=request.user), pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Заметка успешно удалена!')
        return redirect('notes_app:main')

    return render(request, 'notes_app/delete_note.html', {'object': note})

def note_list_view(request):
    sort_order = request.GET.get('sort', 'new')  # Получаем параметр сортировки из запроса

    if sort_order == 'new':
        notes = Notes.objects.all().order_by('-created_at')  # Сортировка от новых к старым
    else:
        notes = Notes.objects.all().order_by('created_at')  # Сортировка от старых к новым

    return render(request, 'notes_app/notes_list.html', {'notes': notes})