# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings

class Blog(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=1000)
	pv = models.PositiveIntegerField(default=0)
	pub_date = models.DateTimeField(auto_now_add=True, null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)

	def add_pv(self):
		self.pv += 1
		self.save(update_fields=['pv'])

	def __str__(self):
		if self.id:
			return '[%d]%s(%s)%s' % (self.id, self.title, self.author, self.pub_date)
		return  '%s(%s)' % (self.title, self.author)
			
class Comment(models.Model):
	content = models.CharField(max_length=1000, null=True)
	author = models.CharField(max_length=200, null=True)
	pub_date = models.DateTimeField(auto_now_add=True, null=True)

	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
		return '[%d]%s' % (self.id, self.content)