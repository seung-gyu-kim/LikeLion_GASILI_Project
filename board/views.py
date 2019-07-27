from django.shortcuts import render

# Create your views here.

def board_create(request) :
    return render(request,'board_create.html')