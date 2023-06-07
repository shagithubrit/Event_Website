from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('events',views.event,name='events'),
    path('event/<str:slug>',views.eventpost,name='eventpost'),
    path('create_event/', views.create_event, name='create_event'),
    path('add', views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
    
]   