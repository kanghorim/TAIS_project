from . import views
from django.urls import path 

app_name = 'tai'

urlpatterns = [
    path('tai/', views.tai, name='tai'),
    path('tai2/', views.tai2, name='tai2'),
]
