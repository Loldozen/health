from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#from .models import Doctor
from .forms import DoctorSignupForm
from .models import Doctor

# Create your views here.

def signup(request, access):
    if access == 'doctor':
        if request.method == 'POST':
            form = DoctorSignupForm(request.POST)
            if form.is_valid():
                doctor = form.save()
                raw_password = form.cleaned_data.get('password1')
                doctor = authenticate(mdcn=doctor.mdcn,password=raw_password)
                messages.success(request,'Signup successful, please wait for verification before login')
                return redirect('doctor:home')
        else :
            form = DoctorSignupForm()
        return render(request, 'doctor/signup.html', {'form':form})

def home(request):
    #return HttpResponse('This is the homepage, would work on it later')
    return render(request, 'doctor/homepage.html')

@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'doctor/profile.html'
    slug_field = 'slug'
    slug_url_kwarg = 'doctor'
    query_pk_and_slug = True

    def get_queryset(self, **kwargs):
        return Doctor.objects.get(pk=self.request.user.id, name=self.request.user.name)

    def get_object(self, **kwargs):
        #return Doctor.objects.get(pk=self.kwargs['pk'], name=self.kwargs['doctor'])
        return Doctor.objects.get(pk=self.request.user.id, name=self.request.user.name)