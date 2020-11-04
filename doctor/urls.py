from django.urls import path, include
from django.contrib.auth import views as auth_views

from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
