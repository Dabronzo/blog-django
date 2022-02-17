from .models import Coments
from django import forms


class CommentForms(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ('body',)
        