from django import forms
from django.core import validators

class FormLogin(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input Your Username'}),
        label=False
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input Your Password'}),
        label=False
    )

class FormRegister(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'please input your username'}),
        label='Username',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='the caracter lower than 20'),
            validators.MinLengthValidator(8, 'the caracter load an 8')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'please input your email'}),
        label='Email',
        validators=[
            validators.EmailValidator('email not corecct')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'please input our password'}),
        label='Password'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'please input agian our password'}),
        label='Re-Password'
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@gmail.com' not in email:
            raise forms.ValidationError('you should use gmail ')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('Password dosnt match')
        return password