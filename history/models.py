from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserAccount

# Create your models here.

class quiz_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    your_choice = models.CharField(max_length=250)
    currect_choice = models.CharField(max_length=250)
    currect_quiz = models.IntegerField(default=0)
    

