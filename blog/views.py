# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from blog.models import Blog, Comment
from blog.forms import CommentForm, BlogForm, SignupForm, LoginForm
from django.urls import reverse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import serializers

# sign up user
def signup_user(request):
	if request.method == 'POST':
		signup_form = SignupForm(request.POST)
		if signup_form.is_valid():
			user = signup_form.save(commit=False)
			#make hashers password
			user.password = make_password(signup_form.cleaned_data['password'])
			user.save()
			return redirect(reverse('homepage'))
	else:
		signup_form = SignupForm()
	context = {"signup_form": signup_form}
	return render(request, 'blog/signup.html', context)

def login_view(request):
	form = LoginForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect(reverse('mybloglist'))
		else:
			return redirect(reverse('login_error'))
	context = {"form":form}
	return render(request, 'blog/login.html', context)

# @login_required
def mybloglist(request):
	myblog_list = Blog.objects.filter(author=request.user)
	context = {"blog_list": myblog_list, "username": request.user}
	return render(request, 'blog/bloglist.html', context)

# @login_required
def jump_userbloglist(request, blog_id, blog_author):
	blog_author = Blog.objects.get(id=blog_id).author
	blog_list = Blog.objects.filter(author=blog_author)
	context = {"blog_list": blog_list, 'username': blog_author}
	return render(request, 'blog/bloglist.html', context)

def logout_view(request):
	logout(request)
	return redirect(reverse('homepage'))

def login_error(request):
	return render(request, 'blog/login_error.html')

def display_error(request):
	return render(request, 'blog/display_error.html')

# @login_required
def homepage(request):
	blog_list = Blog.objects.all()
	context = {"blog_list": blog_list, "request_user": request.user}
	# blog_list. to_json()
	# return HttpResponse("OK")
	# title_json = serializers.serialize("json",Blog.objects.values_list('title'))
	# data = {"title_json":title_json}
	# return JsonResponse(data)
	data_title = list(Blog.objects.values("title"))
	data_author = list(Blog.objects.values("author"))
	data_pub_date = list(Blog.objects.values("pub_date"))
	data = list(Blog.objects.values())
	# return JsonResponse(data, safe=False)
	return render(request, 'blog/homepage.html', context)

#The function of add blog
# @login_required
def add_blog(request):
	title_list = Blog.objects.all().values_list('title', flat=True).order_by('id')
	if request.method == 'POST':
		blog_form = BlogForm(request.POST)
		if blog_form.is_valid():
			blog = blog_form.save(commit=False)
			if blog.title not in title_list:
				blog.save()
				return redirect(reverse('mybloglist'))
			else:
				return redirect(reverse('error'))
	else:
		# blog_form = BlogForm()
		blog_form = BlogForm(initial={'author': request.user})	
	context = {"blog_form": blog_form}
	return render(request, 'blog/form.html', context)

#The function of edit blog
# @login_required
def edit_blog(request, blog_id):
	blog_author = Blog.objects.get(id=blog_id).author
	old_title = Blog.objects.get(id=blog_id).title
	title_list = Blog.objects.exclude(title=old_title).values_list('title', flat=True).order_by('id')
	blog = Blog.objects.get(pk=blog_id)
	if request.method == 'POST':
		edit_form = BlogForm(request.POST, instance=blog)
		if edit_form.is_valid():
			blog = edit_form.save(commit=False)
			if blog.title not in title_list:
				blog.save()
				return redirect(reverse('detail', args=[blog_id]))
			else:
				return redirect(reverse('error'))
	else:
		edit_form = BlogForm(instance=blog)
	context = {'edit_form':edit_form, 'pk':blog_id}
	return render(request, 'blog/form.html', context)

# @login_required
def delete_blog(request, blog_id):
	Blog.objects.filter(pk=blog_id).delete()
	return HttpResponseRedirect(reverse('mybloglist'))

#Display the detail of blog
# @login_required
def detail(request, blog_id):
	blog_page = Blog.objects.filter(pk=blog_id)
	comment_page = Comment.objects.filter(blog_id=blog_id)
	blog_author = Blog.objects.get(id=blog_id).author
	if blog_author == request.user:
		pk = blog_id
	else:
		pk = None
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False) #not save to model, 
			comment.blog_id = blog_id
			comment.save()
			template = loader.get_template('blog/add_comment.html')
			context = {"comment": comment}
			return HttpResponse(template.render(context))
	else:
		comment_form = CommentForm()
		#function for pv
		blog = get_object_or_404(Blog, pk=blog_id)
		blog.add_pv()
	context = {"blog_page": blog_page, "comment_detail": comment_page, 'pk': pk, 'comment_form': comment_form}
	return render(request, 'blog/detail.html', context)