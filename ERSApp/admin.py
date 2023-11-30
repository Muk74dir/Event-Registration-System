from django.contrib import admin
from .models import Event, User, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'location', 'slots_available']
    ordering = ['date', 'time']
    
    def __str__(self):
        return self.title
    
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['event', 'user']
    ordering = ['event', 'user']
    
    def __str__(self):
        return self.user.username + " - " + self.event.title