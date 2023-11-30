from rest_framework import generics
from ERSApp.models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer


class EventListAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    
class UserRegisteredEventsAPIView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Registration.objects.filter(user=user)