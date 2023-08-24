from django.shortcuts import render
from django.http import HttpResponse
from app.models import procedure,patient,physician,fdo
# Create your views here.

def say_hello(request):
    #return HttpResponse('Hello world')
    results=procedure.objects.all()
    print("1")
    print(results)
    return render(request, 'hello.html', {"data": results})
    #return render(request,'hello.html',("data":results))

def index(request):
    return render(request, 'Login.html')

def home(request):
    return render(request,'Home.html')

def Login(request):
    user = int(request.GET["user"])
    pasw = request.GET["pasw"]
  
    print("1")
    # Handle the case where no matching physician is found
    try:
        dr = physician.objects.get(employeeid=user, password=pasw)
        result = patient.objects.get(pcp = user)
        return render(request,'Doctor.html',{"data":result})
    # Process the physician object

    except physician.DoesNotExist:
        try:
            dr = fdo.objects.get(id=user, password=pasw)
            # result = patient.objects.get(pcp = user)
            return render(request,'FDO.html')
    # Process the physician object

        except fdo.DoesNotExist:
        
           return render(request,'Login.html',{"error":'Invalid userid or password'})

def queryp(request):
    id = request.GET["patient"]
    results=patient.objects.get(ssn = id)
    print(results)
    return render(request, 'queryp.html', {"data": results})
