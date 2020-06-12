from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):

    username = forms.CharField(max_length=40, min_length=3, label="Username")
    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField(min_length=2, label="First Name")
    last_name = forms.CharField(min_length=2, label="Last Name")
    password = forms.CharField(max_length=40, min_length=3, label="Password", widget=forms.PasswordInput)
    confirm_pass = forms.CharField(max_length=40, min_length=3, label="Password", widget=forms.PasswordInput)

    def clean(self):

        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        password = self.cleaned_data.get("password")
        confirm_pass = self.cleaned_data.get("confirm_pass")

        if password and confirm_pass and password != confirm_pass:
            raise forms.ValidationError("Passwords do not match.")

        values = {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "password": password
        }

        return values


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)