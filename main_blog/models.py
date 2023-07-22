from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## if user gets deleted all user's posts get deleted.
    img_url = models.CharField(max_length=255, default="https://media.istockphoto.com/id/1047259374/photo/programming-source-code-abstract-background.jpg?b=1&s=612x612&w=0&k=20&c=ujRPoiaJlm5U3WDWcVVa1YVlFIt6Gcjr-RstzOEPbIU=")
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='General')
    status = models.CharField(max_length=100, default='basic') # basic - featured - ad
    approved = models.CharField(max_length=100, default='pending') # pending - declined - approved
    likes = models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')