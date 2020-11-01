from django.urls import path, include
from django.contrib.auth import views as auth_views

from doctor import views 

app_name = 'doctor'

urlpatterns = [
    path('doctor/',views.home, name='home'),
    path('doctor/signup/<str:access>/', views.signup, name='signup'),
    path('doctor/login/', auth_views.LoginView.as_view(template_name='doctor/login.html'), name='login'),
    path('doctor/logout/', auth_views.LogoutView.as_view(template_name='doctor/logout.html'), name='logout'),
    path('doctor/profile/', views.ProfileView.as_view(), name='profile'),
]