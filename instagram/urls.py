from instagram import views
from django.urls import path
from .models import Post
urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.loginUser, name='login-user' ),
    path('logout/', views.logoutUser, name='logout-user' ),
    path('register/', views.registerUser, name='register-user' ),
    path('profile/', views.createProfile, name='create-profile')
]