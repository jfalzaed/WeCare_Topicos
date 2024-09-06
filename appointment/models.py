from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

#Model to store the appointment details
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=15)
    date_options = [
        ("date1", "August 26 3PM"),
        ("date2", "August 29 1PM"),
        ("date3", "August 31 10AM"),
        ("date4", "September 2 11AM"),
        ("date5", "September 11 9AM"),
        ("date6", "September 23 4PM"),
        ("date7", "September 30 2:30PM"),

    ]

    appointment_date = models.CharField(max_length=20, choices=date_options, default="August 26 3PM")

    def __str__(self):
        return self.patient_name
 
#Model to store the reminder details    
class Reminder(models.Model):
    name = models.CharField(max_length=100, default="Reminder")
    reminder_date = models.DateField()
    reminder_title = models.CharField(max_length=100, default="Reminder")
    reminder_message = models.CharField(max_length=200)
    reminder_email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reminder_title