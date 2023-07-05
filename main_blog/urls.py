from django.urls import path
from .views import HomeView, ArticleView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post")
]
