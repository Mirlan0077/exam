from django import forms
from .models import GuestBookEntry

class GuestBookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestBookEntry
        fields = ['author_name', 'author_email', 'entry_text']
        labels = {
            'author_name': 'Имя',
            'author_email': 'Email',
            'entry_text': 'Текст',
        }
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'entry_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
