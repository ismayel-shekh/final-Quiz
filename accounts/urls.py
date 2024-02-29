from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, activate_account
# from .views import profile
from .views import profile, UserPasswordChangeView, UserupdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update_profile/', UserupdateView.as_view(), name='update_profile'),
    path('profile/', profile, name='profile'),
    path('Change/password/', UserPasswordChangeView.as_view(), name='pass_change'),
     path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'),
]
