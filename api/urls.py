from django.urls import path
from .views import EventList, EventDetail, UserRegistration, UserRegisteredEvents

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:event_id>/register/', UserRegistration.as_view(), name='user-register-event'),
    path('user/events/', UserRegisteredEvents.as_view(), name='user-registered-events'),
]
