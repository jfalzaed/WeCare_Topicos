from django import forms
from .models import Appointment

#Form to take the appointment details
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'patient_name', 
            'patient_email', 
            'patient_phone', 
            'appointment_date',
            ]
        
class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = [
            'reminder_date', 
            'reminder_title', 
            'reminder_message', 
            'reminder_email',
            ]
        widget = {
            'reminder_date': forms.DateInput(attrs={'type': 'datetime-local'}),
        }