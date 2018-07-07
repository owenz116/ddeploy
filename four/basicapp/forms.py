from django import forms
from django.contrib.auth.models import User
from basicapp.models import UPI

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')
class UPIform(forms.ModelForm):
    class Meta:
        model = UPI
        fields = ('portfolio_site','profile_pic')
