import math
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board, Comment
from accounts.models import CustomUser
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
            print("----")
            print(request.POST[key])
            if len(request.POST[key]) == 0 or request.POST[key] is None :
                return render(request, 'board_new.html', {'error': '빈칸이 있습니다.'})
    '''
    if request.method == 'POST':
        boards = Board()

        if request.user.id is None :
            return render(request, 'accounts/login.html', {'error': '게시물 작성을 위해 로그인해주세요.'})
        else :
            boards.userId = request.user.id

        boards.title = request.POST['title']
        boards.order_price = request.POST['order_price']
        boards.body = request.POST['body']
        boards.category = request.POST['category']
        boards.state = "판매중"
        
        count = 0 
        for file in request.FILES :
            if count == 0 :
                fileStr = "file"
            else :
                fileStr = "file" + str(count)
            
            file = request.FILES[fileStr]
            filename = rand_str()+".PNG"
            print(filename)
            module_dir = os.path.dirname(__file__)  # get current directory
            upload_path = module_dir.split('\\board')
            
            fp = open('%s/%s' % (upload_path[0]+"\\media\\images", filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            if count == 0 :
                boards.image = 'images/'+filename # POST로 전달한 이미지로
            elif count == 1 :
                boards.image1 = 'images/'+filename
            elif count == 2 :
                boards.image2 = 'images/'+filename
            elif count == 3 :
                boards.image3 = 'images/'+filename
            elif count == 4 :
                boards.image4 = 'images/'+filename
            elif count == 5 :
                boards.image5 = 'images/'+filename

            count = count + 1

    
        # 보완 - 로그인 상태 아닐 경우,
        #if(request.user.username  is None)
        
        print(request.user.id )
        #boards.userId = request.user.id 

        ## 수정필요 ## 
       
        boards.save()
        return redirect('/board/test/' + str(boards.id)) # URL 경로 board로 
        
def test(request, board_id):
        comment = Comment.objects.filter(post=board_id)
        board_detail = get_object_or_404(Board, pk=board_id)
        return render(request,'test.html',{'board' : board_detail, 'comment' : comment})

def csstest(request) :
    return render(request,'csstest.html')
    
def board(request):
        boards = Board.objects
        boards_list = Board.objects.all()
        paginator = Paginator(boards_list,3)
        if(request.GET.get('page') == None):
            page=1
        else:
            page = int(request.GET.get('page'))
    
        posts = paginator.get_page(page)
        page_range = 5 #페이지 범위 지정 예 1, 2, 3, 4, 5 / 6, 7, 8, 9, 10
        current_block = math.ceil(page/page_range) #해당 페이지가 몇번째 블럭인가
        start_block = (current_block-1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
        return render(request, 'board.html',{'boards' : boards , 'posts':posts , 'p_range':p_range , 'page': page})

def createcomment(request, board_id):
        #board = get_object_or_404(Board, pk=board_id) #게시글들에서 하나 뽑음

        comments = Comment()
        comments.userId = request.user.id
        comments.author = request.user.nickname
        comments.text = request.POST['text']
        comments.price = request.POST['price']
        comments.post = board_id
        comments.save()

        return redirect('test', board_id)

def chart(request, board_id):
    return render(request, 'chart.html')