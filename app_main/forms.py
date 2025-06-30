from django import forms
from .models import Comment

class CommentForm(forms.Form):
    email = forms.CharField(max_length=40, label='ایمیل', required=True, widget=forms.EmailInput)
    content = forms.CharField(label='نظر', widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, label='نام کابری', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=150, label='رمز عبور',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    