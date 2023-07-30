from django import forms
from .models import Post, Category

choises = Category.objects.all().values_list('name', 'name')

choise_list = []

for item in choises:
    choise_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'img_url', 'category', 'header_image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'img_url': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choise_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AdminPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'img_url', 'category', 'status', 'approved', 'header_image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'img_url': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choise_list, attrs={'class': 'form-control'}),\
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'approved': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }