from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignupForm , LoginForm , CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    loginform = AuthenticationForm
    context = {
        'loginform':loginform,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        signupform = CustomUserCreationForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        signupform  = CustomUserCreationForm()
    context = {
        'signupform' : signupform,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, request.POST)
        if loginform.is_valid():
            auth_login(request, loginform.get_user())
            return redirect('articles:index')
    else:
        loginform = AuthenticationForm()
    context = {
        'loginform':loginform,
    }
    return render(request, 'articles/index.html', context)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def logout(request):
    if request.method =="POST":
        auth_logout(request)
        return redirect('accounts:index')

@login_required
def delete(request):
    request.user.delete()
    messages.success(request, '회원 탈퇴가 완료되었습니다.')
    return redirect('accounts:index')