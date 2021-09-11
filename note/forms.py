from django import forms
from tinymce.widgets import TinyMCE

from note.models import Note


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'body']

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'label': "Title"
        }
    ))
    body = forms.CharField(widget=TinyMCE(
        attrs={
            'class': 'form-control form-control-user',
            'label': 'Body'
        }
    ))
