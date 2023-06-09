from django.shortcuts import render, HttpResponse
from datetime import datetime
from noticeBoard.models import AdminNotice
from django.contrib import messages

# Create your views here.
def notice(request):
    notices = AdminNotice.objects.all()
    return render(request, 'notice.html', {'notices' : notices})

def adminNotice(request):
    notices = AdminNotice.objects.all()
    if request.method == "POST":
        notice = request.POST.get('notice')
        adminNotice = AdminNotice(notice=notice, date=datetime.today())
        adminNotice.save() 
        messages.success(request, 'Notice has been posted!')
    return render(request, 'adminNotice.html', {'notices' : notices})



