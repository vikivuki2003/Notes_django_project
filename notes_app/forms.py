from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from notes_app.models import Notes


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', '<PASSWORD>', '<PASSWORD>')

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'content')
