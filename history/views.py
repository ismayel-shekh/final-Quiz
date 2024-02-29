from django.shortcuts import render
from . import models
from accounts.models import UserAccount
# Create your views here.
def historyView(request):
    history = models.quiz_history.objects.filter(user = request.user)
    userAccountget = models.UserAccount.objects.get(user = request.user)
    print(userAccountget.score)

    leader = models.UserAccount.objects.all()
    
    return render(request, 'history.html', {'data': history, 'user_data': userAccountget})