from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm

# Create your views here.

def form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_form')
    else:
        form = AppointmentForm()
    return render(request, 'fill_appointment.html', {'form': form})


def success_form(request):
    return render(request, 'success_form.html')