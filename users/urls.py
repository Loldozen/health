from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views,forms

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    #path('user/login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=forms.PatientLoginForm ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', views.patient_login, name='login'),
    path('profile/edit/', views.editProfile, name='edit_profile')
]
