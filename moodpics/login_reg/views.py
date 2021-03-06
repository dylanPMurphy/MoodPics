from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages
# Create your views here.

def index(request):
    if 'userid' in request.session.keys() is not None:
        return redirect('/feed')
    else:
        return render(request, 'index.html')

def register(request):
    if request.method =="POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            
            
            # include some logic to validate user input before adding them to the database!
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
            
            # be sure you set up your database so it can store password hashes this long (60 characters)
            # make sure you put the hashed password in the database, not the one from the form!
            newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], password=pw_hash, email=request.POST['email'])
            request.session['userid'] = newUser.id
            return redirect('/feed') 
            #Create an account

def reg_success(request):
    return render(request, 'successful_REG.html')


def login(request):
    if request.method =="POST":
        user = User.objects.filter(email=request.POST['login_uname'])
        if user and request.POST['login_pass']:
            logged_user = user[0] 

            if bcrypt.checkpw(request.POST['login_pass'].encode(), logged_user.password.encode()):

                request.session['userid'] = logged_user.id

                return redirect('/feed')
            else:
                messages.error(request, "Username or password incorrect")
                return redirect('/')
        else:
            messages.error(request, "Username or password incorrect")
            return redirect('/')

def success(request):

    context = {
        'session_user':User.objects.get(id=request.session['userid'])
    }
    return render(request, 'successful_LOGIN.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
