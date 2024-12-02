from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('logout/', logout_view, name='logout'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('addpost', AddPostView.as_view(), name="addpost"),
    path('addcat', AddCatView.as_view(), name="addcat"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="editpost"),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name="deletepost"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>/', LikeView, name='like'),
]
