from django.shortcuts import render, redirect, HttpResponse
from login_reg.models import *
from .forms import *
from .models import *
from colorthief import ColorThief
import sys
from urllib.request import urlopen
# Create your views here.

def index(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.all().order_by('-created_at')
    }
    return render(request, 'feed.html', context)

def newPost(request):
    if request.method == "POST":
        form.save()
        redirect("/")
    form = NewPostForm()
    context = { "newPostForm": form }
    return render(request, "newpost.html", context)
def getColors(newPost):
    color_thief_on_post = ColorThief(newPost.img)
    dom_color_list = color_thief_on_post.get_palette(quality=1)
    Pallette.objects.create(photo=newPost, color_1=('#%02x%02x%02x' % dom_color_list[0]),color_2=('#%02x%02x%02x' % dom_color_list[1]), color_3=('#%02x%02x%02x' % dom_color_list[2]), color_4=('#%02x%02x%02x' % dom_color_list[3]))
def submitPost(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid'])
        
    }
    
    np = Post.objects.create(
        title = request.POST['title'],
        img = request.FILES['img'],
        mood = request.POST['mood'],
        poster = User.objects.get(id =request.session['userid'])
        
    )
    getColors(np)
    return redirect('/feed')



def brilliant(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.filter(mood="B").order_by('-created_at')
    }
    return render(request, 'feed.html', context)

def gloom(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.filter(mood="G").order_by('-created_at')
    }
    return render(request, 'feed.html', context)

def lush(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.filter(mood="L").order_by('-created_at')
    }
    return render(request, 'feed.html', context)
def vibrant(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.filter(mood="V").order_by('-created_at')
    }
    return render(request, 'feed.html', context)
def mystique(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.filter(mood="M").order_by('-created_at')
    }
    return render(request, 'feed.html', context)
def turbulant(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "posts":Post.objects.filter(mood="T").order_by('-created_at')
    }
    return render(request, 'feed.html', context)

def post_page(request, post_id):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid']),
        "post": Post.objects.get(id=post_id),
    }
    return render(request, 'post.html', context)
    
def like_post(request,post_id):
    authenticated_user=User.objects.get(id=request.session['userid'])
    this_post = Post.objects.get(id=post_id)
    this_post.likers.add(authenticated_user)
    return HttpResponse("Successful")
