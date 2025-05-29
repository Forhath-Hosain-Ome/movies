from django import forms
from .models import *


class moviecreate(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['title', 'description', 'release_year', 'is_available', 'genra']