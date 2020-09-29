from django.shortcuts import render,redirect
from .tasks import send_email_task
# Create your views here.

def mail(request):

    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']
        fromMail=request.POST['from']
        toArr=request.POST['to']

        toArr=[toArr]

        try:
            send_email_task(subject,message,fromMail,toArr)
            return redirect('/')
        except:
            print("An Error has Occurred")
            return None

    else:
        return render(request,'mail.html')

def index(request):

    return render(request,"index.html")