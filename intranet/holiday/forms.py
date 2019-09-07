from django import forms
from django.contrib.auth.models import User
from holiday.models import UserProfileInfo

class VacationForm(forms.Form):
    vacation_begining = forms.DateField()
    vacation_length = forms.IntegerField()
    vacation_status = forms.IntegerField()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_superuser')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_photo', 'profile_vacation_left', 'profile_vacation_new')
