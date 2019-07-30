from django.shortcuts import render

# query Set 결과물을 [ list ] 로 변환한다
def chart(request):
    return render(request, 'home.html')