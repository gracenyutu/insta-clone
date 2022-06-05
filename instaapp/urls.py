from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('search/', views.search, name='search'),
    path('createprofile/',views.create_profile,name="signup"),
    path('login/',views.Login,name="Login"),
    path('logout/',views.Logout,name="Logout"),
    path('profile/',views.profile,name="profile"),
    path('follow/<int:id>/<str:username>/',views.follow,name="follow")
]
