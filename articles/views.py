from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.

def init(request):
    return redirect('articles:index')

def index(request):
    context = {

    }
    return render(request, 'articles/index.html', context)