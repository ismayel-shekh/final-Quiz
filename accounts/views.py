from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import UserAccount, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import UserAccount
from .forms import UserFrom
from django.views import View
# Create your views here.

# class UserRegistrationView(FormView):
#     template_name= 'accounts/user_registration.html'
#     form_class = UserFrom
#     success_url = reverse_lazy('profile')
    

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return super().form_valid(form) # self called valid function
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        messages.success(self.request, "Successfully logged in.")
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/user_pass_change.html'
    success_url = reverse_lazy('profile')

@login_required
def profile(request):
    user_profile = UserAccount.objects.get(user = request.user)
 
    
    # # print(data.account.email)
    # return render(request, 'accounts/profile.html', {'form': data, 'history': history})

    return render(request, 'accounts/profile.html',{ 'user': user_profile})


class UserupdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    





from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib import messages



class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserFrom
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # Activate the user account automatically
        user.save()

        # Get current site to build the complete activation link
        current_site = get_current_site(self.request)

        # Send email with login link
        subject = 'Activate Your Account'
        message = render_to_string('accounts/user_email.html', {
            'user': user,
            'protocol': self.request.scheme,  # Use the scheme (http/https) from the request
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = form.cleaned_data['email']
        email = EmailMessage(subject, message, to=[to_email])
        email.send()
        messages.success(self.request, "Dear user, please go to your email inbox and click on the received activation link to confirm and complete the registration. Note: Check your spam folder.")
        login(self.request, user)
        return super().form_valid(form)


# from django.http import HttpResponseBadRequest
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth import get_user_model
# from django.shortcuts import redirect

# def activate_account(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = get_user_model().objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
#         user = None

#     if user and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
#         return redirect('login')  # Redirect to login page after successful activation
#     else:
#         messages.error(request, "Activation link is invalid!")
#         print('not not currect token Account')
#         return redirect('home')
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages

def activate_account(request, uidb64):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None:
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for your email confirmation. Now you can login to your account.")
        return redirect('login')  # Redirect to login page after successful activation
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect('home')  # Redirect to home page if activation fails