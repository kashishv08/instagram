from django.http import HttpResponse
from .forms import LoginForm, ProfileModelForm, PostModelForm
from .models import Post, Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            exists = User.objects.filter(username=username).exists()
        if exists:
            messages.info(request, "Already have account! Please login")
            return redirect('/login')
        User.objects.create_user(username=username, password=password)
        return redirect('/')    
    else:
        form = LoginForm()    

    return render(request, "authForm.html", {"is_login": False, "form" : form})

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

        user = User.objects.filter(username=username).first()
        if not user:
            messages.error(request, "Please Register!!")
            return redirect('/register')

        authenticated_user = authenticate(request, password=password, username=username)
        if authenticated_user:
            login(request=request, user=authenticated_user)
            messages.success(request, "Successfully login :)")
            return redirect("/")
        messages.error(request, "Username or Password should be correct!")   
        return redirect('/login')
    else:
        form = LoginForm()    
        
    return render(request, "authForm.html", {"is_login": True, "form" : form})

def logoutUser(request):
    logout(request)
    messages.info(request, "Logged Out!!")
    return redirect('/')

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def createProfile(request):
    if request.method == 'POST':
        form = ProfileModelForm(request.POST or None, request.FILES or None)
        if(form.is_valid()): 
            username = request.user.username
            user = User.objects.filter(username=username).first()
            profile = Profile.objects.filter(user=user).first()
            if profile:
                messages.info(request, "Profile Already exists")
                return redirect("/login")
            else:
                profile = form.save(commit=False)
                profile.user = request.user
                form.save()
                messages.success(request, "Profile created :)")
                return redirect('/')
    form = ProfileModelForm()
    return render(request, 'profileForm.html', {'form' : form})

def createPost(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        form.save()
        messages.success(request, "Post created")
        return redirect("/")
    return render(request,'PostForm.html', {"form": form})

def editPost(request, id):
    post = Post.objects.get(id=id)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Form edited")
        return redirect("/")
    return render(request, 'PostForm.html', {"form": form, 'post': post})


def likePost(request, id):
    post = Post.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        exist = post.likes.filter(id=request.user.id).exists()
        if exist:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect("/")