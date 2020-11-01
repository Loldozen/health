from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views,forms

app_name = 'users'

urlpatterns = [
    path('user/', views.home, name='home'),
    path('user/signup/<str:access>/', views.signup, name='signup'),
    path('user/profile/', views.ProfileView.as_view(), name='profile'),
    #path('user/login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=forms.PatientLoginForm ), name='login'),
    path('user/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('user/login/', views.patient_login, name='login'),
    path('user/profile/edit/', views.editProfile, name='edit_profile')
    
]