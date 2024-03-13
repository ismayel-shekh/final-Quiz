from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('details<int:id>/', views.QuizView.as_view(), name='quiz_detail'),
    # path('history/<int:c_id>/<str:c_value>/', views.history, name='history'),
     path('check_answer/<int:q_id>/<str:selected_choice>/', views.check_answer, name='check_answer'),
    #  path('', views.sendemail, name='submit')
    path('review/', views.quiz_review, name='review'),
    path('create_category/', views.createCatagory, name='create_category'),
    path('create_quiz/', views.createquiz, name='create_quiz'),
    path('create_question/', views.createquestion, name='create_question'),
]