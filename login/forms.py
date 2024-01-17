
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser



class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    username = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"Enter your username"}), label="Username")
    password = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"Enter your password"}), label="Password")
    


    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"Enter your first name"}), label="First Name")
    class Meta:
        model = CustomUser
        fields = ['first_name', 'username', 'last_name', 'email', 'gender', 'city', 'country', 'password1', 'password2']
