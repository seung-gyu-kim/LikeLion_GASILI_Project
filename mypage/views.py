from django.shortcuts import render, redirect
from board.models import Board, Comment

# Create your views here.
def mypageBlog(request):
    if request.user.is_authenticated:
        posts = Board.objects.filter(userId = request.user.id)
        return render(request, 'mypage/mypageBlog.html', {'posts': posts})
    else:
        return redirect('login')

def mypageComment(request):
    if request.user.is_authenticated:
        posts = Comment.objects.filter(userId = request.user.id)
        return render(request, 'mypage/mypageComment.html', {'posts': posts})
    else:
        return redirect('login')