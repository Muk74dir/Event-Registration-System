from django.urls import path, include
from .views import HomeView, UserCreateView, LogInView, LogOutView

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
