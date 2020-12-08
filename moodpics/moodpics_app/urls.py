from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('brilliant/', views.brilliant),
    path('gloom/', views.gloom),
    path('lush/', views.lush),
    path('vibrant/', views.vibrant),
    path('mystique/', views.mystique),
    path('turbulant/', views.turbulant),
    path('posts/new', views.newPost),
    path('posts/new/submit', views.submitPost),
    path('posts/<int:post_id>', views.post_page),
    path('posts/<int:post_id>/like', views.like_post),
    path('posts/<int:post_id>/comment', views.comment_post),



]

