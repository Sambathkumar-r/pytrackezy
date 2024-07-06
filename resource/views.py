from django.http import HttpResponse
from django.shortcuts import render
from .models import Resource

# Create your views here.
def index(request):
    resource = Resource.objects.all()
    return render(request,'index.html',{'resource':resource})