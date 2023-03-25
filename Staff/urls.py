from django.urls import path
from .views import leave_application

urlpatterns = [
    path('leave_application/', leave_application, name='leave_application'),
]
