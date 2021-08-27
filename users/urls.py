from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<str:pk>/', views.profile, name='user-profile')
]