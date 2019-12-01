from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    search = request.GET.get('search', '')
    if search:
        posts = posts.filter(how_many=search)

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'posts':posts, 'search':search})

@login_required
def my_post_list(request):
    posts = Post.objects.filter(creator=request.user)
    return render(request, 'my_post_list.html', {'posts':posts})
    
@login_required
def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    request_user = request.user
    comments = post_detail.comments.all()
    return render(request, 'post_detail.html',{'post':post_detail, 'user':request_user, 'comments':comments})

# def post_new(request):
#     post = Post()
#     post.title = "admin12345"
#     return render(request,'post_new.html',{'post':post})

# def post_create(request):
#     user = request.user
#     if user.is_authenticated:
        # post= Post()
        # post.title = request.GET['title'] # 제목저장
        # post.text = request.GET['text'] # 본문저장
        # post.how_many = request.GET['how_many'] # 몇명 저장
        # post.creator = user #유저 정보 저장
        # post.save()
        # return redirect('/posts/detail/' + str(post.id))
    # else:
    #     return render(request, 'login.html')

@login_required
def post_new(request):
    user = request.user
    if request.method == 'GET':
        return render(request,'post_new.html')
    elif request.method == 'POST' and user.is_authenticated:
        post= Post()
        post.title = request.POST['title'] # 제목저장
        post.text = request.POST['text'] # 본문저장
        post.how_many = request.POST['how_many'] # 몇명 저장
        post.creator = user #유저 정보 저장
        post.save()
        return redirect('/posts/detail/' + str(post.id))
    else:
        return render(request, 'login.html')      

@login_required
def post_delete(request, post_id):
    post_to_delete = get_object_or_404(Post, pk=post_id)
    post_to_delete.delete()
    return redirect('/posts/myposts/')

# def post_update(request,post_id):
#     post = get_object_or_404(Post, pk = post_id)
#     return render(request,'post_new.html',{'post':post})

# def post_update_func(request,post_id):
#     post = get_object_or_404(Post, pk = post_id)
#     post.title = request.GET['title'] # 제목저장
#     post.text = request.GET['text'] # 본문저장
#     post.how_many = request.GET['how_many'] # 몇명 저장
#     post.creator = request.user #유저 정보 저장
#     post.save()
#     return redirect('/posts/detail/' + str(post.id))
# 조원준 : 끝

@login_required
def post_update(request, post_id):
    user = request.user
    if request.method == 'GET':
        post = get_object_or_404(Post, id = post_id)
        return render(request,'post_new.html', {'post':post})
    elif request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.how_many = request.POST['how_many']
        post.creator = request.user
        post.save()
        return redirect('/posts/detail/' + str(post.id))
 
@login_required
def post_comment_create(request, post_id):
    user = request.user
    if request.method=='POST' and user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        comment = Comment()
        comment.post = post
        comment.creator = user
        comment.message = request.POST['message']
        comment.save()
        return redirect('/posts/detail/' + str(post.id))
    else:
        return render(request, 'login.html')

@login_required
def post_comment_delete(request, comment_id):
    comment_to_delete = get_object_or_404(Comment, id=comment_id)
    post_id = comment_to_delete.post.id
    comment_to_delete.delete()
    return redirect('/posts/detail/' + str(post_id))

def index_return(request):
    return render(request, 'index.html')

def main_return(request):
    return render(request, 'main.html')

