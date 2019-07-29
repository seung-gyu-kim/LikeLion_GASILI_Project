from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
import math
# Create your views here.

def board_create(request) :
    return render(request,'board_create.html')

def test(request, board_id) :
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request,'test.html',{'board' : board_detail})

def board(request):
    boards = Board.objects
    boards_list = Board.objects.all()
    paginator = Paginator(boards_list,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    page_range = 5
    current_block = math.ceil(int(page)/page_range)
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    return render(request, 'board.html',{'boards' : boards , 'posts':posts , 'p_range': p_range})