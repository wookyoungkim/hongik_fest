from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('myposts/', views.my_post_list, name='my_post_list'),
    path('detail/<int:post_id>/',views.post_detail,name='detail'), # 글 자세히 보기
    path('new/',views.post_new,name="new"), # 글 쓰기
    path('<int:post_id>/delete/',views.post_delete, name="delete"), # 글 삭제
    path('<int:post_id>/update/',views.post_update, name="update"),
    path('<int:post_id>/comments/', views.post_comment_create, name='post_comment_create'), # 덧글 생성
    path('comments/<int:comment_id>/', views.post_comment_delete, name='post_comment_delete'), # 덧글 삭제
]
