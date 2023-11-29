from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserCreateFrom, RegistrationForm, EventForm
from .models import Event, Registration

class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')
    
class UserCreateView(CreateView):
    model = User
    form_class = UserCreateFrom
    template_name = 'signup.html'
    success_url = '/'
    
class LogInView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return '/'
        
        
        
class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
