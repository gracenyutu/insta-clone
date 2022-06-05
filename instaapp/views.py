from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile, Image

# Create your views here.
def home(request):
    return render(request, 'instaapp/home.html')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'instaapp/profile.html',{'profile':profile,'profile_of_user':True})

def search(request):
    search = request.GET['username']
    profiles = Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles,'username':search}
    return render(request,'instaapp/search.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('profile')
    return render(request, 'instaapp/login.html')

def create_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        image = request.FILES['image']
        user = User.objects.create_user(username=username,password=password)
        profile = Profile.objects.create(user=user,photo=image)
        if profile:
            messages.success(request,'Profile created Kindly Login')
            return redirect("Login")
    return render(request, 'instaapp/signup.html')

def Logout(request):
    logout(request)
    return redirect('Login')

def follow(request,id,username):
    profile = Profile.objects.get(id=id)
    profile.followers.add(request.user)
    login_profile = Profile.objects.get(user=request.user)
    login_profile.followings.add(profile.user)
    return redirect(f'search?username={username}')