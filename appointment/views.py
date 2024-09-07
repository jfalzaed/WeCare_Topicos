from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm
import os.path
import datetime as dt
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dateutil import parser
from django.http import HttpResponse, JsonResponse
from .forms import AppointmentForm, ReminderForm
from .models import Reminder
from django.contrib.auth.decorators import login_required

# Create your views here.

#Function to read the form and save the data in the database
def form(request):
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            creds = None

            if os.path.exists("token.json"):
                creds = Credentials.from_authorized_user_file("token.json")

            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file("client_secret_158471176816-dc1tg1eho7hbef8ehsu6rgpv7tucnp13.apps.googleusercontent.com.json", SCOPES)
                    creds = flow.run_local_server(port=0)

                with open("token.json", "w") as token_file:
                    token_file.write(creds.to_json())

            service = build("calendar", "v3", credentials=creds)

            timeDateTime = parser.isoparse(form.cleaned_data['appointment_date'])
            endtime = timeDateTime + dt.timedelta(hours=1)
            endtime = endtime.isoformat()
            event = {
                "summary": "Mental health appointment",
                "start": {"dateTime": form.cleaned_data['appointment_date'], "timezone": "GMT-5"},
                "end": {"dateTime": endtime, "timezone": "GMT-5"},
                "reminders" : {
                    'useDefault': False,
                    'overrides' : [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'email', 'minutes': 10},
                        {'method': 'popup', 'minutes': 10}
                    ]
                }
            }

            event = service.events().insert(calendarId=form.cleaned_data['patient_email'], body=event, sendUpdates='all').execute()
            
            return redirect('success_form')
        else:
            print(form.errors)
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