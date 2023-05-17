from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	groups = forms.SelectMultiple(attrs={'class':'form-select' ,'style': 'width: 100%'})
	class Meta:
		model = User
		fields = ['username','password1', 'password2', 'email','groups']
		help_texts = {k:"" for k in fields }