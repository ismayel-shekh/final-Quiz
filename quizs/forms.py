from django import forms
from .models import Quiz, Review
from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields =['Name', 'rating']
        fields = '__all__'

class createCatagory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields ='__all__'

class CreateQuiz(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields ='__all__'

class createQuestion(forms.ModelForm):
    class Meta:
        model = models.Question
        fields ='__all__'
        