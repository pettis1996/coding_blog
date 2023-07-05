from django.urls import path
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
]
