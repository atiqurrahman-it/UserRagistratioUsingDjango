from django import forms
from django.contrib.auth.models import User


class UserRgistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label="username",widget=forms.TextInput(
        attrs={'placeholder': 'Write Your username','class': 'form-control'}))

    email = forms.EmailField(max_length=200,label='email',widget=forms.EmailInput(
        attrs={'placeholder': 'Write Your email','class': 'form-control'}))
    first_name = forms.CharField(max_length=100,label="first_name",widget=forms.TextInput(
        attrs={'placeholder': 'Write Your first name','class': 'form-control'}))
    last_name = forms.CharField(max_length=100,label="last_name",widget=forms.TextInput(
        attrs={'placeholder': 'Write Your last name','class': 'form-control'}))


    password =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password','class': 'form-control'}))
    confrim_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter  confirm_password','class': 'form-control'}))


    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

        


