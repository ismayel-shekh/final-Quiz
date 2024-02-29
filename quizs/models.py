from django.db import models
from accounts.models import UserAccount
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Question(models.Model):
    question = models.CharField(max_length=250)
    point = models.IntegerField()
    choice_1 = models.CharField(max_length=250)
    choice_2 = models.CharField(max_length=250)
    choice_3 = models.CharField(max_length=250)
    choice_4 = models.CharField(max_length=250)
    currect_choice = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐⭐'),

]
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    rating = models.CharField(choices =STAR_CHOICES, max_length =15)
    def __str__(self):
        return self.quiz.title