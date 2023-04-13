from django.shortcuts import render, redirect

# Create your views here.

def init(request):
    return redirect('articles:index')

def index(request):
    context = {

    }
    return render(request, 'articles/index.html', context)