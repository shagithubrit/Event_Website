from django.shortcuts import render,HttpResponse
from events.models import Event

# Create your views here.
def event(request):
    return render(request, 'base.html')
