from django.urls import path, include
from .views import HomeView, UserCreateView, LogInView, LogOutView, UserDashboardView
from .views import EventListView, EventDetailView, RegisterForEvent, UnregisterFromEvent

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('event_detail/<int:pk>/', EventDetailView.as_view(), name='event_detail'),   
    path('event/register/<int:pk>/', RegisterForEvent.as_view(), name='register'),
    path('event/unregister/<int:pk>/', UnregisterFromEvent.as_view(), name='unregister'),
    path('dashboard/', UserDashboardView.as_view(), name='dashboard'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
