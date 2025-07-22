from django import forms
from .models import MoodEntry

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'How are you feeling today?',
                'class': 'w-full p-4 rounded-lg border border-purple-200 bg-white/80 backdrop-blur-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-purple-300 h-40 resize-none',
            })
        }
