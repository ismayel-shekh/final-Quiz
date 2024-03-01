from django.shortcuts import render, redirect
from django.views.generic import DetailView
from . import models
from . import forms
from history.models import quiz_history
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


# Create your views here.

class QuizView(DetailView):
    model = models.Quiz
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'quizs'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.object
        reviews = quiz.reviews.all()
        review_form = forms.ReviewForm()
        context['reviews'] = reviews
        context['reviews_form'] = review_form

        return context

# def history(request, c_id, c_value):
#     qus = models.Question.objects.get(pk=c_id)
#     x = c_value
#     print(qus.question)    
#     print(x)
#     user_acount = models.UserAccount.objects.get(user = request.user)
#     if c_value == qus.currect_choice:
#         user_acount.score += qus.point


from django.http import JsonResponse

def history(request, c_id, c_value):
    qus = models.Question.objects.get(pk=c_id)
    x = c_value
    print(qus.question)    
    print(x)
    user_acount = models.UserAccount.objects.get(user=request.user)
    
    response_data = {'result': 'incorrect'}

    if c_value == qus.currect_choice:
        user_acount.score += qus.point
        response_data['result'] = 'correct'
    
    return JsonResponse(response_data)


from django.http import JsonResponse

def check_answer(request, q_id, selected_choice):
    question = models.Question.objects.get(pk=q_id)
    correct_choice = question.currect_choice
    print(correct_choice)
    print(selected_choice)
    user_account = models.UserAccount.objects.get(user=request.user)
    print(user_account)
    is_correct = selected_choice == correct_choice
    score = 0
    his = quiz_history(
        user = user_account.user,
        question = question.question,
        your_choice = selected_choice,
        currect_choice = correct_choice,
    )
    his.save()

    if is_correct:
        user_account = models.UserAccount.objects.get(user=request.user)
        user_account.score += question.point
        user_account.currect_quiz += 1

        user_account.save()
        score = user_account.score
        print(user_account.score)
    return JsonResponse({'is_correct': is_correct, 'score': score})

def sendemail(request):
    user_account = models.UserAccount.objects.get(user=request.user)
    send_transaction_email(request.user, user_account.score, "succesfuly complite quiz", 'quiz_email.html' )
    return redirect('home')

def send_transaction_email(user, user_account, subject, template):
    message = render_to_string(template,{
        'user': user,
        'user_account': user_account,

    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

from django.contrib import messages
def quiz_review(request):
    user_account = models.UserAccount.objects.get(user=request.user)
    print(user_account.currect_quiz)
    send_transaction_email(request.user, user_account, "succesfuly complite quiz", 'quiz_email.html' )
    messages.success(request, "if you want to show your sammary Chack your email address")
    if request.method == 'POST':
        review = forms.ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            return redirect('history')
    else:
        review = forms.ReviewForm()
    return render(request, 'review.html', {'form': review})

# from django.core.mail import send_mail
# class quiz_reviewView(DetailView):
#     model = models.Review

#     template_name = 'review.html'
#     context_object_name = 'review_app'
#  def post(self, request, *args, **kwargs):
#         # Add logic to handle the review form submission
#         review_form = forms.ReviewForm(data=self.request.POST)
#         quiz = self.get_object()

#         if review_form.is_valid():
#             new_review = review_form.save(commit=False)
#             new_review.quiz = quiz
#             new_review.reviewer = request.user
#             new_review.save()

#             # Send email when the review is submitted
#             subject = "New Quiz Review Submitted"
#             message = f"A new review has been submitted for the quiz: {quiz.title}"
#             send_mail(subject, message, 'from@example.com', [request.user.email])

#         return self.get(request, *args, **kwargs)