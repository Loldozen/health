from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#from .models import Doctor
from .forms import PatientSignupForm, PatientLoginForm
from .models import Patient

# Create your views here.

def signup(request, access):
    if access == 'user':
        if request.method == 'POST':
            form = PatientSignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=user.email,password=raw_password)
                messages.success(request,'Signup successful, you can login now')
                return redirect('users:login')
        else :
            form = PatientSignupForm()
        return render(request, 'users/signup.html', {'form':form})

def home(request):
    #return HttpResponse('This is the homepage, would work on it later')
    return render(request, 'users/homepage.html')

@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Patient
    context_object_name = 'user'
    template_name = 'user/profile.html'
    slug_field = 'slug'
    slug_url_kwarg = 'user'
    query_pk_and_slug = True

    def get_queryset(self, **kwargs):
        return Patient.objects.get(pk=self.request.user.id, name=self.request.user.name)

    def get_object(self, **kwargs):
        #return Doctor.objects.get(pk=self.kwargs['pk'], name=self.kwargs['doctor'])
        return Patient.objects.get(pk=self.request.user.id, name=self.request.user.name)

def patient_login(request):
    
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user, backend='doctor.backends.UserAuthenticationBackend' )
                    messages.success(request, 'Login successful')
                    return redirect('users:home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = PatientLoginForm()
    return render(request, 'users/login.html', {'form':form})


"""def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='doctor.backends.UserAuthenticationBackend')
            return redirect('users:home')
    else:
        form = PatientLoginForm()
    return render(request, 'users/login.html', {'form':form})
"""
def editProfile(request):
    edit = get_object_or_404(Patient, id=request.user.id)
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')
        else: 
            messages.error(request, 'Error updating your profile')
    else:
        form = PatientSignupForm(instance=edit)
        return render(request, 'users/signup.html', {'form':form})