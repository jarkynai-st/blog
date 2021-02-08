from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('blog/',blog_page,name='blog'),
    path('post/',post_page,name='post'),
    path('blogs_p/<int:blog_id>/',blog_posts)
]