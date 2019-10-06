#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'blog_poll'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/result/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote')
]