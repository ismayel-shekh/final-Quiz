from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('details<int:id>', views.QuizView.as_view(), name='quiz_detail'),
]
    # path('', views.home, name='home'),

#     path('category/<str:category_slug>/', views.home, name='category_wice_quiz'),


# from django.shortcuts import render
# from quiz.models import Category, Quiz

# def home(request, category_slug = None):
#     data = Quiz.objects.all()
#     if category_slug is not None:
#         category = Category.objects.get(name = category_slug)
#         data = Quiz.objects.filter(catagory=category)
#     categories = Category.objects.all()
#     return render(request, 'home.html',{'data': data, 'category': categories,})