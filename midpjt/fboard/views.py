from django.shortcuts import render

# Create your views here.
def notification(request):
    return render(request, 'fboard/notification.html')

def notification_view(request) :
    return render(request, 'fboard/notification_view.html')

def news(request):
    return render(request, 'fboard/news.html')

# def community(request):
#     return render(request, 'community.html')

def news_page(request):
    return render(request, 'fboard/news_page.html')

