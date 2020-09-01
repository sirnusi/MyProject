from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(null=True, upload_to='profilepics')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-pub_date']
        

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('dashboard')

class Comment(models.Model):
    content = models.TextField()
    name = models.CharField(blank=True, null=True, unique=True, max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='article_post', blank=True)
    thumbnail = models.ImageField(upload_to='profilepics')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dashboard')