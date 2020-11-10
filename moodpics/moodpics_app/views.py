from django.shortcuts import render
from login_reg.models import *
from .forms import *
from .models import *
# Create your views here.

def index(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid'])
        
    }
    return render(request, 'feed.html', context)

def newPost(request):
    form = NewPostForm()
    context = { "newPostForm": form }
    return render(request, "newpost.html", context)

def getColors(request):
    pass