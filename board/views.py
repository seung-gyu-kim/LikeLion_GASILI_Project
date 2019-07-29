import math
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board

# Create your views here.

def board_create(request) :
    return render(request,'board_create.html')

def test(request, board_id) :
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request,'test.html',{'board' : board_detail})

def board(request):
    boards = Board.objects
    boards_list = Board.objects.all()
    paginator = Paginator(boards_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'board.html',{'boards' : boards , 'posts':posts})