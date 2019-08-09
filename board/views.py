import math
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board, Comment

# Create your views here.


def board_new(request) :
        return render(request,'board_new.html')

def create(request) :
    for key in request.POST:
        if len(request.POST[key]) == 0:
            return render(request, 'board_new.html', {'error': '빈칸이 있습니다.'})

    if request.method == 'POST':
        boards = Board()
        boards.title = request.POST['title']
        boards.order_price = request.POST['order_price']
        boards.date = timezone.datetime.now()
        boards.body = request.POST['body']
        boards.category = request.POST['category']
        boards.state = "판매중"

        # 보완 - 로그인 상태 아닐 경우,
        #if(request.user.username  is None)
        boards.userName = request.user.username 
        ## 수정필요 ## 
        boards.image = 'images/선풍기.jpg' # POST로 전달한 이미지로 
        boards.save()
        return redirect('/test/' + str(boards.id)) # URL 경로 board로 
        
def test(request, board_id):
        comment = Comment.objects.filter(post=board_id)
        board_detail = get_object_or_404(Board, pk=board_id)
        return render(request,'test.html',{'board' : board_detail, 'comment' : comment})

def board(request):
        boards = Board.objects
        boards_list = Board.objects.all()
        paginator = Paginator(boards_list,3)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'board.html',{'boards' : boards , 'posts':posts})

def createcomment(request, board_id):
        #board = get_object_or_404(Board, pk=board_id) #게시글들에서 하나 뽑음

        comments = Comment()
        comments.author = request.user.username
        comments.text = request.POST['text']
        comments.price = request.POST['price']
        comments.created_date = timezone.datetime.now()
        comments.post = board_id

        comments.save()

        return redirect('test', board_id)