from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile, Post, Reels, Story
from django.db.models import Q

# Create your views here.
def home(request):
    posts = Post.objects.filter(Q(profile__followers=request.user) & ~Q(likes=request.user))
    story = Story.objects.filter(profile__followers=request.user)
    context = {"posts":posts,'stories':story}
    return render(request, 'instaapp/home.html',context)

def profile(request,id=None):
    if not request.user.is_authenticated:
        return redirect("Login")
    if id is not None:
        profile_id = Profile.objects.get(id=id)
        posts = Post.objects.filter(profile=profile_id)
        posts_num = posts.count()
        profile = Profile.objects.get(user=request.user)
        profileimage = profile.profile_picture.url
    else:
        profile_id = Profile.objects.get(user=request.user)
        posts = Post.objects.filter(user=request.user)
        posts_num = posts.count()
        profile = Profile.objects.get(user=request.user)
        profileimage = profile.profile_picture.url
    return render(request,'instaapp/profile.html',{'profile':profile_id,'profileimage':profileimage,'profile_of_user':True,'posts':posts,'posts_num':posts_num})

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
    login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        login_profile.followings.remove(profile.user)
    else:
        profile.followers.add(request.user)
        login_profile.followings.add(profile.user)
    return redirect(f'search?username={username}')

def upload_post(request):
    if request.method == 'POST':
        post = request.FILES['post']
        profile = Profile.objects.get(user=request.user)
        posts = Post.objects.create(user=request.user,image=post,profile=profile)
        if posts:
            messages.success(request,"post uploaded successfully!")
    return render(request,'uploadposts.html')

def like_post(request,id):
    post = Post.objects.filter(id=id)
    if request.user in post[0].likes.all():                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        post[0].likes.remove(request.user)
    else:
        post[0].likes.add(request.user)
    return redirect("home")

def upload_reel(request):
    logout(request)
    if request.method == 'POST':
        reel = request.FILES['reel']
        profile = Profile.objects.get(user=request.user)
        reels = Reels.objects.create(reel=reel)
        if reels:
            messages.success(request,"reel uploaded successfully!")
    return render(request,'uploadreels.html')

def reels(request):
    reels = Reels.objects.all()
    return render(request,'reels.html',{'reels':reels})

def upload_story(request):
   if request.method == 'POST':
        story = request.POST['story']
        profile = Profile.objects.get(user=request.user)
        story_upload = Story.objects.create(story=story,profile=profile)
        if story_upload:
            messages.success(request,"story uploaded successfully!")
        return render(request,'UploadStory.html')