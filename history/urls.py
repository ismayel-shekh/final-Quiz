from django.urls import path
from . import views
urlpatterns = [
    path('history/', views.historyView, name='history')
]
