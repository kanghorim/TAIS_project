from . import views
from django.urls import path 

app_name = 'comm'

urlpatterns = [
    path('community/', views.community, name='community'),
    path('<str:board_no>/community_view/', views.community_view, name='community_view'),
    path('community_write/', views.community_write, name='community_write'),
    path('community_writeOk/', views.community_writeOk, name='community_writeOk'),
]
