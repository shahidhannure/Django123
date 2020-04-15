from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index (request):
    return render(request,'index.html')
    #return HttpResponse('This is homepage')
    
def about (request):
    return render(request,'about.html')
    #return HttpResponse('This is aboutpage')

def contact (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address') 
        contact = Contact(name=name,email=email,number=number,address=address,date= datetime.today())
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse('This is contactpage')        