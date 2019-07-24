from django.shortcuts import render

# Create your views here.

def board_main(request) :
    return render(request,'board_main.html')