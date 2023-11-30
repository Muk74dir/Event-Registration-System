from django.urls import path
from .views import EventListAPIView, EventDetailAPIView, UserRegistrationAPIView, UserRegisteredEventsAPIView

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='event_list_api'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event_detail_api'),
    path('register/', UserRegistrationAPIView.as_view(), name='user_registration_api'),
    path('registered-events/', UserRegisteredEventsAPIView.as_view(), name='user_registered_events_api'),
    
]
