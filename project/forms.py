__author__ = 'Parth Shah'
from django.contrib.auth.models import User
from django import forms
from .models import Post


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class PostUploadForm(forms.ModelForm):
    photo = forms.FileField()
    caption = forms.CharField()

    class Meta:
        model = Post
        fields = ['photo', 'caption']

