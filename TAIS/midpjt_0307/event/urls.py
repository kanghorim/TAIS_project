from . import views
from django.urls import path 

app_name = 'event'

urlpatterns = [
    path('event/', views.event, name='event'),
    path('event_view/', views.event_view, name='event_view'),
]
