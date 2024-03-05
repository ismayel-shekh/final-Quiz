from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount

class UserFrom(UserCreationForm):
    mobile_no = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields =['username','first_name', 'last_name','email','password1', 'password2', 'mobile_no',]
    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            mobile_no = self.cleaned_data.get('mobile_no')
            image = self.cleaned_data.get('image')
            UserAccount.objects.create(
                user = our_user,
                mobile_no = mobile_no,

            )
        return our_user
        
class UserUpdateForm(forms.ModelForm):
    mobile_no = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields =['first_name','last_name','email', 'mobile_no',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None
            if user_account:
                user = user_account.user
                self.fields['first_name'].initial = user.first_name
                self.fields['last_name'].initial = user.last_name
                self.fields['email'].initial = user.email
                self.fields['mobile_no'].initial = user_account.mobile_no


                # print(user_account.last_name)


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_account.first_name = self.cleaned_data['first_name']
            user_account.last_name = self.cleaned_data['last_name']
            user_account.email = self.cleaned_data['email']
            user_account.mobile_no = self.cleaned_data['mobile_no']


            user_account.save()
        return user

