from django.contrib import admin
from django.urls import path
from noticeBoard import views

urlpatterns = [
    path("", views.notice, name='noticeBoard'),
    path("adminNotice", views.adminNotice, name='noticeBoard'),
    path("notice", views.notice, name='noticeBoard'),
   
   
]