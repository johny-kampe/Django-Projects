from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employee(request):
    return HttpResponse("This is the Employee Page")

def employeeNew(request):
    return HttpResponse("This is the New Employee Page")

def profile(request):
    return render(request, 'employee/profile.html')
