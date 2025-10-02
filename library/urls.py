from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path('statistics/', views.search_statistics, name='statistics'), # /library/statistics/
    path('', views.mental_health_library, name='library')            # /library/
]