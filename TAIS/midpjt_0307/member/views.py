from django.http import JsonResponse
from django.shortcuts import render

from member.models import User_Info

# Create your views here.

def login(request):
    return render(request, 'member/login.html')

def addaccount(request):
    return render(request, 'member/addaccount.html')
