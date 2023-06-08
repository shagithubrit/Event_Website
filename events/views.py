from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from events.models import Event

# Create your views here.
def event(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'events.html',context)

def eventpost(request,slug):
    event = Event.objects.filter(id=id).first()
    context = {'event':event}
    return render(request,'event.html',context)

def create_event(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request,'create_event.html',context)

def ADD(request):
    if request.method== 'POST':
        event_title = request.POST.get('event_title')
        event_desc = request.POST.get('event_desc')
        slug = request.POST.get('slug')
        event_createdby = request.POST.get('event_createdby')

        ev=Event(
            event_name=event_title,
            event_desc=event_desc,
            slug=slug,
            event_createdby=event_createdby,
        )
        ev.save()
        return redirect('create_event')

def Edit(request):
    events = Event.objects.all()
    context = {'events':events}
    return redirect(request,'create_event',context)

def Update(request,id):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_desc = request.POST.get('event_desc')
        slug = request.POST.get('slug')
        event_createdby = request.POST.get('event_createdby')

        ev=Event(
            id=id,
            event_name=event_title,
            event_desc=event_desc,
            slug=slug,
            time=datetime.now(),
            event_createdby=event_createdby,
        )
        ev.save()
        return redirect('create_event')
    return redirect(request,'create_event.html')

def Delete(request,id):
    events=Event.objects.filter(id=id)
    events.delete()
    context = {'events':events}
    return redirect('create_event')


def search(request):
    query = request.GET['query']
    events = Event.objects.filter(event_name__icontains=query)
    params = {'events':events}

    return render(request,'search.html',params)
     