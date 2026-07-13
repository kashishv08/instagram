from instagram import views
from django.urls import path
from .models import Post
urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.loginUser, name='login-user' ),
    path('logout/', views.logoutUser, name='logout-user' ),
    path('register/', views.registerUser, name='register-user' ),

    path('profile/create', views.createProfile, name='create-profile'),
    path('profile/edit', views.editProfile, name='edit-profile'),
    path('profile/<int:id>', views.profile, name='view-profile'),
    path('profile/search', views.searchUser, name='search-user'),

    path('post/', views.createPost, name='create-post'),
    path('post/<int:id>/edit', views.editPost, name='edit-post'),
    path('post/<int:id>/delete', views.deletePost, name='delete-post'),
    path('post/<int:id>/like', views.likePost, name='like-post'),
    path('post/<int:id>/save', views.savePost, name='save-post'),

    path('follow/<int:id>', views.follow, name='follow'),
]