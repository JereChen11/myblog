from django import forms
from django.forms import ModelForm, Textarea, TextInput
from blog.models import Blog, Comment
from django.contrib.auth.forms import AuthenticationForm, User

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		widgets = {
			'content': Textarea(attrs={'cols': 270, 'rows': 2}),
		}

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'author', 'content']
		widgets = {
			'title': Textarea(attrs={'cols': 50, 'rows': 5}),
			'author': forms.HiddenInput(),
			'content': Textarea(attrs={'cols': 100, 'rows': 5}),
		}

class SignupForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'username': Textarea(attrs={'cols': 60, 'rows': 1}),
			'password': Textarea(attrs={'cols': 60, 'rows': 1}),
		}

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)