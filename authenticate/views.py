from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# Create your views here.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        
        
        userToAuth = authenticate(request, username=username, password=password)
        
        if userToAuth is not None:
            login(request, userToAuth)
            # Checking if a GET next request exists
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('/')
            
        else:
            messages.error(request, 'One or more Credentials are incorrect')
            return redirect('auth_app:login')  
            
    return render(request, 'auths/login.html')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        #username = request.POST['username']
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')
        
        if User.objects.filter(username=username):
            messages.error(request, 'Username already in use choose another!')
            return redirect('auth_app:register')
        if User.objects.filter(email=email):
            messages.error(request, 'Email already exist!')
            return redirect('auth_app:register')
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 character')
            return redirect('auth_app:register')
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('auth_app:register')
        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric!')
            return redirect('auth_app:register')
        else:
            newUser =  User.objects.create_user(username=username, email=email, password=password2, first_name=fname, last_name=lname)
            newUser.save()
            # Add customer to a group automatically
            group = Group.objects.get(name='users')
            newUser.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)

            
            return redirect('auth_app:login')
    return render(request, 'auths/register.html')

def signOut(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')


@login_required(login_url='auth_app:login') #add redirect functionality
@allowed_users(allowed_roles=['admin'])
def superUserDo(request):
    return HttpResponse('This is a clear case of privilege escalation!!!!!!')