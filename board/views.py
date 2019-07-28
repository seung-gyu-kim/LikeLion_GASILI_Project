from django.shortcuts import render
from .models import Board
# Create your views here.

def board_create(request) :
    return render(request,'board_create.html')

def test(request) :
    boards = Board.objects
    return render(request,'test.html',{'boards' : boards})

def board(request):
    boards = Board.objects
    return render(request, 'board.html',{'boards' : boards})