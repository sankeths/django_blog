from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>/', views.post, name="post"),
]
