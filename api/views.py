from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from ERSApp.models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, id=event_id)
        user = self.request.user
        serializer.save(event=event, user=user)

class UserRegisteredEvents(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(registration__user=user)
