from django.shortcuts import render
from django.views.generic import DetailView
from . import models
from . import forms
# Create your views here.
class QuizView(DetailView):
    model = models.Quiz
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'quizs'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # quiz = self.object
        # reviews = quiz.reviews.all()
        # review_form = forms.ReviewForm()
        # context['reviews'] = reviews
        # context['reviews_form'] = review_form

        return context