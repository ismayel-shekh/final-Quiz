from django.shortcuts import render
from quizs.models import Category, Quiz
from accounts.models import UserAccount

def home(request, category_slug = None):
    data = Quiz.objects.all()
    if category_slug is not None:
        category = Category.objects.get(name = category_slug)
        data = Quiz.objects.filter(catagory=category)
    categories = Category.objects.all()
    return render(request, 'home.html',{'data': data, 'category': categories,})

def leader(request):
    data = UserAccount.objects.all().order_by('-score')
    return render(request, 'leader.html', {'data': data})