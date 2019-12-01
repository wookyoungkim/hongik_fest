from django.urls import path
from . import views


app_name = 'bars'
urlpatterns = [
    path('', views.bar_list, name='bar_list'),
    path('<int:bar_id>/detail/', views.bar_detail, name='bar_detail'),
    path('<int:bar_id>/likes/', views.bar_like, name='bar_like'),
]
