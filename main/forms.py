from django import forms
from .models import Contact
from .models import EmotionReport

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }


class EmotionReportForm(forms.ModelForm):
    class Meta:
        model = EmotionReport
        fields = ['user_name', 'stress', 'focus', 'mood', 'fatigue', 'calmness']