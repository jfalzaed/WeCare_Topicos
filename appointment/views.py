from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import AppointmentForm, ReminderForm
from .models import Reminder
from django.contrib.auth.decorators import login_required

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


#function to create a reminder
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('create_reminder')
    else:
        form = ReminderForm()
    return render(request, 'create_reminder.html', {'form': form})


"""@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminder_list.html', {'reminders': reminders})"""