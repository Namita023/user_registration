from django import forms
from app.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','address']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}