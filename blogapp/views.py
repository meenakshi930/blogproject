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
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogapp/create_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blogapp/signup.html', {'form': form})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogapp/post_detail.html', {'post': post})