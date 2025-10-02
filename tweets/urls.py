from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('signup/', views.signup, name='signup'),
]