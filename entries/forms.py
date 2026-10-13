from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'autocomplete': 'name',
                    'placeholder': 'e.g. Alex Morgan',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'autocomplete': 'email',
                    'placeholder': 'you@example.com',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': 'Write something worth remembering...',
                }
            ),
        }
