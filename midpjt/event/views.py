from django.shortcuts import render

# Create your views here.
def event(request):
    return render(request, 'event/event.html')

def event_view(request) :
    return render(request, 'event/event_view.html')