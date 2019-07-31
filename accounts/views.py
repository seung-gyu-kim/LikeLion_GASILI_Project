from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        for key in request.POST:
            if len(request.POST[key]) == 0:
                return render(request, 'accounts/signup.html', {'error': '빈칸이 있습니다.'})
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': '이미 있는 아이디 입니다.'})
            except CustomUser.DoesNotExist:
                try:
                    user = CustomUser.objects.get(nickname=request.POST['nickName'])
                    return render(request, 'accounts/signup.html', {'error': '이미 있는 닉네임 입니다.'})
                except CustomUser.DoesNotExist:
                    # 관리자 권한 부여 여부 결정
                    boolValue = False
                    if 'is_superuser' in request.POST.keys():
                        boolValue = True
                    # user 모델에 저장
                    user = CustomUser.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1'],
                        last_name=request.POST['lastName'],
                        first_name=request.POST['firstName'],
                        gender=request.POST['gender'],
                        birthdate=request.POST['birthdate'],
                        nickname=request.POST['nickName'],
                        is_staff=boolValue,
                        is_superuser=boolValue)
                    auth.login(request, user)
                    return redirect('index')
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': '아이디 혹은 비밀번호가 틀렸습니다.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'accounts/signup.html')

def update(request):
    if request.method == "GET" and request.user.is_authenticated:   # 로그인 상태로 update 접속 시
        return render(request, 'accounts/update.html')
    elif request.method == "POST":  # update 제출 시 달라진 부분 회원 정보 수정
        # if request.user.username != request.POST['username']:
        #     try:
        #         user = CustomUser.objects.get(username=request.POST['username'])
        #         return render(request, 'accounts/update.html', {'error': '이미 있는 아이디 입니다.'})
        #     except CustomUser.DoesNotExist:
        #         request.user.username = request.POST['username']
        # if request.user.gender != request.POST['gender']:
        #     request.user.gender = request.POST['gender']
        # if request.user.last_name != request.POST['lastName']:
        #     request.user.last_name = request.POST['lastName']
        # if request.user.first_name != request.POST['firstName']:
        #     request.user.first_name = request.POST['firstName']
        # if request.user.birthdate != request.POST['birthdate']:
        #     request.user.birthdate = request.POST['birthdate']    # 다른 필드 바꾸는 내용. 필요하면 주석 해제
        if request.user.nickname != request.POST['nickName']:
            try:
                user = CustomUser.objects.get(nickname=request.POST['nickName'])
                return render(request, 'accounts/update.html', {'error': '이미 있는 닉네임 입니다.'})
            except CustomUser.DoesNotExist:
                request.user.nickname=request.POST['nickName']
        request.user.save()
        return redirect('index')
    else:   # 로그인하지 않았을 시
        return render(request, 'accounts/login.html')

# 비밀번호 변경
def changePassword(request):
    context= {}
    if request.method == 'POST':
        current_password = request.POST.get('origin_password')
        user = request.user
        if user.check_password(current_password):
            new_password = request.POST.get('password1')
            password_confirm = request.POST.get('password2')
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                exitWindow = 1
                return render(request, 'accounts/changePassword.html', {'exitWindow': exitWindow})
            else:
                context.update({'error':'새로운 비밀번호를 다시 확인해주세요.'})
        else:
            context.update({'error':'현재 비밀번호가 일치하지 않습니다.'})

    return render(request, 'accounts/changePassword.html', context)