from django.shortcuts import render
from login_reg.models import *
# Create your views here.

def index(request):
    context = {
        "authenticated_user": User.objects.get(id=request.session['userid'])
        
    }
    return render(request, 'feed.html', context)
