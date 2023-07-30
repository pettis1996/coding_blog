import os
from django.http import HttpResponseRedirect, FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import AdminPostForm, PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date', '-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)   
        context["cat_menu"] = cat_menu
        
        return context
 
class AdminDashboardView(ListView):
    model = Post
    template_name = 'admin_dashboard.html'
    ordering = ['-post_date', '-id'] 

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)   

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post 
    form_class = EditForm
    template_name = 'update_post.html'

class AdminUpdatePostView(UpdateView):
    model = Post 
    form_class = AdminPostForm
    template_name = 'admin_update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category 
    template_name = 'add_category.html'
    fields = '__all__' 
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    categories_menu = Category.objects.all()
    return render(request, 'categories_menu.html', {'categories_menu': categories_menu})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    liked = False 
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

def AboutMeView(request):
    skills = [
        {
            'title': 'Frontend',
            'icon': 'bi-arrows-fullscreen',
            'items': ['HTML5', 'CSS3', 'JS', 'SASS/SCSS', 'ReactJS', 'Thymeleaf', 'Jinja']
        },
        {
            'title': 'Backend',
            'icon': 'bi-hdd-network',
            'items': ['Java', 'Java Springboot', 'Python', 'Django', 'FastAPI', 'C | C++']
        },
        {
            'title': 'Databases | Servers',
            'icon': 'bi-database-check',
            'items': ['MySQL', 'MongoDB', 'MariaDB', 'AWS', 'Postman', 'DBeaver']
        },
        {
            'title': 'Other',
            'icon': 'bi-clipboard2-data',
            'items': ['Figma', 'Lunacy', 'Github | GitLab', 'Jira', 'Jenkins', 'Kubernetes', 'Docker']
        },
    ]

    socials = [
        {
            "title": "Github",
            "url": "https://github.com/pettis1996",
            "icon": "bi bi-github"
        },
        {
            "title": "Instagram",
            "url": "https://instagram.com/",
            "icon": "bi bi-instagram"
        },
        {
            "title": "Youtube",
            "url": "https://youtube.com/",
            "icon": "bi bi-youtube"
        },
        {
            "title": "LinkedIn",
            "url": "https://www.linkedin.com/in/paraskevas-pettis-112024237/",
            "icon": "bi bi-linkedin"
        },
    ]

    projects = [
        {
            "project_name": "Blog Web Application",
            "url": "https://github.com/pettis1996/coding_blog",
            "description": "A blog posting web application made with the python django framework.",
        },
        {
            "project_name": "Sudolver",
            "url": "https://github.com/pettis1996/sudolver",
            "description": "Sudoku solver using a free API from Rapid API website.",
        },
        {
            "project_name": "University Management System",
            "url": "https://github.com/pettis1996/university-management-system",
            "description": "Web Application for Univarsity Management System. (Uni Project)",
        },
        {
            "project_name": "Songs Search Engine",
            "url": "https://github.com/pettis1996/SongsSearchEngine",
            "description": "Application in Java for searching song lyrics using the Lucene library.",
        },
    ]

    return render(request, 'about_me.html', {"skills": skills, "socials": socials, "projects": projects})

# TODO: fix this 
def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, '1.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment; filename="1.pdf"'
            return response
    else:
        raise Http404("File not found")