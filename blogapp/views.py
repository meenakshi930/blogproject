from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # Admin → see all posts
            posts = Post.objects.all().order_by('-created_at')
        else:
            # Normal user → see only their posts
            posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        # Not logged in → show all posts (optional, you can restrict if you want)
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blogapp/home.html', {'posts': posts})
@login_required


def signup(request):
    pass
def create_post(request):
    pass
def post_details(request):
    pass
