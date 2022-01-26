from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def resource(request):
    return render(request, 'resource.html')

def findtutors(request):
    return render(request, 'findtutors.html')  
