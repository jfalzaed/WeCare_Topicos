from django.contrib import admin
from .models import Appointment, Reminder

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Reminder)