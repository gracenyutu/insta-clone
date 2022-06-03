from django.shortcuts import render, redirect
from .models import Profile, Image

# Create your views here.
def home(request):
    return render(request, 'instaapp/home.html')

def profile(request):
    # if not request.user.is_authenticated:
    #     return redirect("Login")
    # if id is not None:
    #     profile_id = Profile.objects.get(id=id)
    #     profile = Profile.objects.get(user=request.user)
    #     profileimage = profile.profile_picture.url
    # else:
    #     profile_id = Profile.objects.get(user=request.user)
    #     profile = Profile.objects.get(user=request.user)
    #     profileimage = profile.profile_picture.url
    return render(request,'instaapp/profile.html')

def search(request):
    if not request.user.is_authenticated:
        return redirect("Login")
    profile = Profile.objects.get(user=request.user)
    profileimage = profile.profile_picture.url
    profile = Profile.objects.get(user=request.user)
    profileimage = profile.profile_picture.url
    search = request.GET['username']
    profiles = Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles,'username':search,"profileimage":profileimage}
    return render(request,'instaapp/search.html',context)

def Login(request):
    return render(request, 'instaapp/login.html')

def create_profile(request):
    return render(request, 'instaapp/signup.html')