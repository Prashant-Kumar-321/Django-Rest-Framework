from django.urls import path 

from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'), # localhost:8000/api/
    path('echo/', views.echo_users_request, name='echo-user') # localhost:8000/echo/
]