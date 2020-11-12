from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('post/new', views.newPost),
    
    path('post/new/submit', views.submitPost),
    path('api/get_colors', views.getColors)
]

