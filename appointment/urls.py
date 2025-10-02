from django.urls import path
from . import views

app_name = "appointment"

urlpatterns = [
    path('create/', views.form, name='fill_appointment'),                                       # /appointments/create/
    path('filed/', views.success_form, name='success_form'),                                    # /appointments/filed/
    path('reminders/create/', views.create_reminder, name='create_reminder'),                   # /appointments/reminder/create/
    path('reminders/list/', views.reminder_list, name='reminder_list'),                         # /appointments/reminder/list/
    path('reminders/edit/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),       # /appointments/reminder/edit/1/
    path('reminders/delete/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'), # /appointments/reminder/delete/1/
]