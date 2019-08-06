import math
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
import os
import random
import string

# Create your views here. 
def rand_str():
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def board_new(request) :
    return render(request,'board_new.html')

def create(request) :
    '''
    for key in request.POST:
            if len(request.POST[key]) == 0:
                return render(request, 'board_new.html', {'error': '빈칸이 있습니다.'})
    '''

    if request.method == 'POST':
        boards = Board()
        boards.title = request.POST['title']
        boards.order_price = request.POST['order_price']
        boards.date = timezone.datetime.now()
        boards.body = request.POST['body']
        boards.category = request.POST['category']
        boards.state = "판매중"
        
        count = 0 
        for file in request.FILES :
            if count == 0 :
                fileStr = "file"
            else :
                fileStr = "file" + str(count)
            count = count + 1

            file = request.FILES[fileStr]
            filename = rand_str()+".PNG"
            print(filename)
            module_dir = os.path.dirname(__file__)  # get current directory
            upload_path = module_dir.split('\\board')
            
            fp = open('%s/%s' % (upload_path[0]+"\\media\\images", filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
        boards.image = 'images/'+filename # POST로 전달한 이미지로 
        
        
        # 보완 - 로그인 상태 아닐 경우,
        #if(request.user.username  is None)
        boards.userName = request.user.username 
        ## 수정필요 ## 
       
        boards.save()
        return redirect('/test/' + str(boards.id)) # URL 경로 board로 
        
def test(request, board_id) :
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request,'test.html',{'board' : board_detail})

def csstest(request) :
    return render(request,'csstest.html')
def board(request):
    boards = Board.objects
    boards_list = Board.objects.all()
    paginator = Paginator(boards_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'board.html',{'boards' : boards , 'posts':posts})