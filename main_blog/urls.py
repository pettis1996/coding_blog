from django.urls import path
from .views import AdminUpdatePostView, HomeView, AdminDashboardView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('admin_dashboard/', AdminDashboardView.as_view(), name="admin_dashboard"),
    path('admin_dashboard/edit/<int:pk>', AdminUpdatePostView.as_view(), name="admin_update_post"),
    path('categories-menu', CategoryListView, name="categories_menu"),
]   
