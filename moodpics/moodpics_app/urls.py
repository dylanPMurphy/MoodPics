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

    path('post/new', views.newPost),
    
    path('post/new/submit', views.submitPost),
    path('api/get_colors', views.getColors)
]

