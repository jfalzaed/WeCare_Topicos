from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm, ReminderForm

# Create your views here.

#Function to read the form and save the data in the database
def form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_form')
    else:
        form = AppointmentForm()
    return render(request, 'fill_appointment.html', {'form': form})


#function to render the success page after the form is filled
def success_form(request):
    return render(request, 'success_form.html')

def create_reminder(request):
    """if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminder_list')  # Redirige a la lista de recordatorios
    else:
        form = ReminderForm()"""
    return render(request, 'create_reminder.html', {'form': form})