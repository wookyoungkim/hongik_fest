from django import forms
from .models import Letter


# Letter을 기반으로 한 Form
class LetterPost(forms.ModelForm):
    class Meta:
        model = Letter
        fields = [
            'text',
        ]