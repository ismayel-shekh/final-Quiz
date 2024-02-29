from django import forms
from .models import quiz_history

class history(forms.ModelForm):
    class Meta:
        model = quiz_history
        fields = '__all__'