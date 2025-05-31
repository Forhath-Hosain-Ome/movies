from django import forms
from .models import *


class moviecreate(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            'title', 'description', 'release_year', 'is_available', 'genra'
            ]

        labels = {
                'Movies': 'Movies',
            }
        help_texts = {
            'release_year': 'Only 2000 to 2026 allowed.',
        }