# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet'),  # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('tweet/delete/<int:id>', views.delete_view, name='delete-tweet'),
    path('tweet/<int:id>', views.tweet_detail, name='tweet-detail'),
    path('tweet/comment/<int:id>', views.save_comment, name='save-comment'),
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='save-comment'),
]