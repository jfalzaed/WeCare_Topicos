from django.urls import path

from . import views

app_name = "Account"

urlpatterns = [
    path('profile/', views.perfil_view, name='perfil'),       # /accounts/profile/
    path('login/', views.login_view, name='login'),           # /accounts/login/
    path('logout/', views.logout_view, name='logout'),        # /accounts/logout/
    path('register/', views.register_view, name='register'),  # /accounts/register/
    path('', views.home, name='home'),                        # /accounts/
]