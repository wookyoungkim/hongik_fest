from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import User, Letter, UserLike
from .forms import LetterPost


# 마이페이지 보기 - 수정
@login_required
def mypage(request):
    user = request.user
    # 받은 쪽지 개수
    letter_to = Letter.objects.filter(letter_to=request.user, delete=False).count()
    # 보낸 쪽지 개수
    letter_from = Letter.objects.filter(letter_from=request.user, delete=False).count()
    return render(request, 'mypage.html', {
        'user':user, 
        'letter_to':letter_to,
        'letter_from':letter_from
    })

# 타유저의 페이지 보기
@login_required
def userpage(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'userpage.html', {'user':user})
 
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                name=request.POST.get('name'), 
                password=request.POST['password1'], 
                profile_image=request.FILES.get('profile_img', None),
                bio=request.POST['bio'],
                phone=request.POST['phone'], 
                gender=request.POST['gender'], 
                profile_open=request.POST['profile_open'],
                )
            if user is not None:
                auth.login(request, user)
                return redirect('/users/mypage/')
    print("회원가입 안됨")
    return render(request, 'signup.html') 

# 로그인을 하지 않은 상태에서 로그인이 필요한 서비스를 이용하고자 할때
def indirect_login(request):
    if request.method == 'GET':
        # 처음 로그인 요청이 들어왔던 페이지 경로를 global 변수에 넣음
        global redirect_url
        redirect_url = request.GET.get('next')
        error_message = '로그인이 필요한 서비스입니다. 로그인해주세요.'
        return render(request, 'login.html', {'error_message':error_message})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user) 
            return redirect(redirect_url)# 처음 요청이 들어왔던 페이지로 다시 리다이렉트(동적으로 변함)
        else:
            error_message = '일시적인 오류로 다시 로그인해주세요.'
            return render(request, 'login.html', {'error_message':error_message})
    error_message = '잘못된 요청입니다. 다시 로그인해주세요.'  
    return render(request, 'login.html', {'error_message':error_message})

# 로그인 페이지에서 로그인 할 때
def direct_login(request):
    if request.method == 'GET':
        error_message = '로그인페이지입니다.'
        return render(request, 'login.html', {'error_message':error_message})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)        
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html', {'user':user})
    error_message = '잘못된 요청입니다. 다시 로그인해주세요.'  
    return render(request, 'login.html', {'error_message':error_message})
        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

# 쪽지 보내기
@login_required
def letter_post(request, user_id):
    if request.user.is_authenticated and request.method == 'POST':
        form = LetterPost(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.letter_to = get_object_or_404(User, id=user_id)
            letter.letter_from = request.user
            letter.save()
            return redirect('/users/letters/from/')
    elif request.method == 'GET':
        letter_to = get_object_or_404(User, id=user_id)
        form = LetterPost()
        return render(request, 'letter_post.html', {'form':form, 'letter_to':letter_to})

# 받은 쪽지 보기(type='to') / 보낸 쪽지 보기(type='from')
@login_required
def letter_list(request, type):
    if type == 'to':
        letter_to_list = Letter.objects.filter(letter_to=request.user, delete=False)
        return render(request, 'letter_list.html', {'letters':letter_to_list})
    elif type == 'from':
        letter_from_list = Letter.objects.filter(letter_from=request.user, delete=False)
        return render(request, 'letter_list.html', {'letters':letter_from_list})
 
@login_required
def letter_to_delete(request, letter_id):
    user = request.user
    letter = get_object_or_404(Letter, id=letter_id)
    letter.delete = True
    letter.save()
    if letter.letter_to == user: 
        return redirect('/users/letters/to/')
    elif letter.letter_from == user:
        return redirect('/users/letters/from/')

# 쪽지 상세보기
@login_required
def letter_detail(request, letter_id):
    user = request.user
    letter = Letter.objects.get(id=letter_id)
    letter.check = True
    letter.save()
    return render(request, 'letter_detail.html', {'letter':letter, 'user':user})

# 유저 목록 (성별에 따른 검색 기능)
def user_list(request):
    users_all = User.objects.filter(profile_open=True)
    paginator = Paginator(users_all, 5)
    page = request.GET.get('page')
    users_list = paginator.get_page(page)
    return render(request, 'user_list.html', {'users_list':users_list})

def user_male(request):
    users_find = User.objects.filter(gender='male', profile_open=True)
    paginator = Paginator(users_find, 5)
    page = request.GET.get('page')
    users_list = paginator.get_page(page)
    return render(request, 'user_list.html', {'users_list':users_list})

def user_female(request):
    users_find = User.objects.filter(gender='female', profile_open=True)
    paginator = Paginator(users_find, 5)
    page = request.GET.get('page')
    users_list = paginator.get_page(page)
    return render(request, 'user_list.html', {'users_list':users_list})


# 유저에게 하트 보내기
@login_required
def like_user(request, user_id):
    user = request.user
    like_user = get_object_or_404(User, id=user_id)
    try:
        preexisiting_like = UserLike.objects.get(userlike_from=user, userlike_to=like_user)
        preexisiting_like.delete()
        return redirect('/users/' + str(like_user.id))
    except UserLike.DoesNotExist:
        userlike = UserLike()
        userlike.userlike_to = like_user
        userlike.userlike_from = user
        userlike.save()
        return redirect('/users/' + str(like_user.id))
