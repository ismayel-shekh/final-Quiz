from django.shortcuts import render
from quizs.models import Category, Quiz

def home(request, category_slug = None):
    data = Quiz.objects.all()
    if category_slug is not None:
        category = Category.objects.get(name = category_slug)
        data = Quiz.objects.filter(catagory=category)
    categories = Category.objects.all()
    return render(request, 'home.html',{'data': data, 'category': categories,})