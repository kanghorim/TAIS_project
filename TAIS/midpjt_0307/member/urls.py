
from . import views
from django.urls import path 

app_name = 'member'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('addaccount/', views.addaccount, name='addaccount'),
    # path('idcheck/', views.idcheck, name='idcheck'),
]
