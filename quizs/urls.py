from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('details<int:id>/', views.QuizView.as_view(), name='quiz_detail'),
    # path('history/<int:c_id>/<str:c_value>/', views.history, name='history'),
     path('check_answer/<int:q_id>/<str:selected_choice>/', views.check_answer, name='check_answer'),
    #  path('', views.sendemail, name='submit')
    path('review/', views.quiz_review, name='review')
]