from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignupForm , LoginForm

# Create your views here.
def index(request):
    loginform = LoginForm
    context = {
        'loginform':loginform,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            username = signupform.cleaned_data['username']
            password = signupform.cleaned_data['password']
            email = signupform.cleaned_data['email']
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            request.session['user_id'] = user.id
            return redirect('accounts:index')
    else:
        signupform = SignupForm()
    return render(request, 'accounts/signup.html',{'signupform':signupform})

def login(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, request.POST)
        if loginform.is_valid():
            auth_login(request, loginform.get_user())
            return redirect('accounts:index')
    else:
        loginform = AuthenticationForm()
    context = {
        'loginform':loginform,
    }
    return render(request, 'accounts/index.html', context)

@login_required
def logout(request):
    if request.method =="POST":
        auth_logout(request)
        return redirect('accounts:index')
