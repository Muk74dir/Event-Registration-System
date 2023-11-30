from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventList, EventDetail, UserRegistration, UserRegisteredEvents

router = DefaultRouter()
router.register('api/', EventViewSet, basename='event')


urlpatterns = [
    path('', include(router.urls), name='event-list'),
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:event_id>/register/', UserRegistration.as_view(), name='user-register-event'),
    path('user/events/', UserRegisteredEvents.as_view(), name='user-registered-events'),
]
