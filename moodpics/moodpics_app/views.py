from django.shortcuts import render, redirect
from login_reg.models import *
from .forms import *
from .models import *
# Create your views here.

def index(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.all()
    }
    return render(request, 'feed.html', context)

def newPost(request):
    if request.method == "POST":
        form.save()
        redirect("/")
    form = NewPostForm()
    context = { "newPostForm": form }
    return render(request, "newpost.html", context)

def submitPost(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid'])
        
    }
    Post.objects.create(
        title = request.POST['title'],
        img = request.FILES['img'],
        mood = request.POST['mood'],
        poster = User.objects.get(id =request.session['userid'])
        
    )
    return redirect('/feed')

def getColors(request):
    pass