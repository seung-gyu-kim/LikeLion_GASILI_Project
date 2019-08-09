from django.shortcuts import render, get_object_or_404
from .models import Service
# Create your views here.

def servicecenter(request):
    services = Service.objects
    return render(request, 'servicecenter.html', {'services' : services})


