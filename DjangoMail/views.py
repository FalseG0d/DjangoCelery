from django.shortcuts import render,redirect
from django.http import HttpResponse
from .tasks import send_email_task
# Create your views here.

def mail(request):

    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']
        fromMail=''
        toArr=request.POST['to']

        toArr=[toArr]

        try:
            send_email_task.delay(subject,message,fromMail,toArr)
            return render(request,'index.html')
        except:
            return HttpResponse("<h1>An Error Has Occured</h1>")

    else:
        return render(request,'index.html')

def index(request):

    return render(request,"index.html")