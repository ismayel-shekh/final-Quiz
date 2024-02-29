from django import forms
from .models import Quiz, Review

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ='__all__'
