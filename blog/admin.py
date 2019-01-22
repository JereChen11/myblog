# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
	pass
    # list_display = ("title", "content")
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
