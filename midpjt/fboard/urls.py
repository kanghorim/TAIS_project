
from . import views
from django.urls import path 

app_name = 'fboard'

urlpatterns = [
    path('notification/', views.notification, name='notification'),
    path('notification_view/', views.notification_view, name='notification_view'),
    path('news/', views.news, name='news'),
    path('news_page/', views.news_page, name='news_page'),

]
