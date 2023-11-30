from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserCreateFrom, RegistrationForm, EventForm
from .models import Event, Registration

class BaseLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'


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

class EventListView(BaseLoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.all()
        user_registered_events = Registration.objects.filter(user=request.user)
        context = {
            'events': events,
            'user_registered_events': user_registered_events,
        }
        return render(request, 'event_list.html', context)

    
class EventDetailView(BaseLoginRequiredMixin, View):
    def get(self, request, pk):
        event = Event.objects.get(id=pk)
        user_registration = Registration.objects.filter(user=request.user, event=event).first()
        context = {
            'event': event,
            'user_registration': user_registration,
        }
        return render(request, 'event_detail.html', context)

    
class RegisterForEvent(BaseLoginRequiredMixin, View):
    def get(self, request, pk):
        if Registration.objects.filter(user=request.user, event=Event.objects.get(id=pk)).exists():
            return redirect('event_detail', pk=pk)
        event = Event.objects.get(id=pk)
        registration = Registration.objects.create(user=request.user, event=event)
        event.slots_available -= 1
        event.save()
        return redirect('event_detail', pk=pk)

    
class UnregisterFromEvent(BaseLoginRequiredMixin, View):
    def get(self, request, pk):
        event = Event.objects.get(id=pk)
        registration = Registration.objects.filter(user=request.user, event=event)
        registration.delete()
        event.slots_available += 1
        event.save()
        return redirect('event_detail', pk=pk)


class UserDashboardView(BaseLoginRequiredMixin, View):
    def get(self, request):
        user_registered_events = Registration.objects.filter(user=request.user)
        context = {
            'user_registered_events': user_registered_events,
        }
        return render(request, 'user_dashboard.html', context)
