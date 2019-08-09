from django.shortcuts import render, redirect
from board.models import Board

# Create your views here.
def mypage(request):
    if request.user.is_authenticated:
        posts = Board.objects.filter(userId = request.user.id)
        return render(request, 'mypage/mypage.html', {'posts': posts})
    else:
        return redirect('login')