from django.shortcuts import get_object_or_404, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Post, Category, Article, Comment
from .forms import PostForm, CommentForm


# Create your views here.

def LikeView(request, id):
    post = get_object_or_404(Article, id=request.POST.get('article_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(f'/blogapp/article/{post.slug}/')
    

class Home(ListView):
    model = Post
    template_name = 'blogapp/home.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:9]
        context['articles'] = Article.objects.all()[:9]
        return context


class About(LoginRequiredMixin, TemplateView):
    template_name = 'blogapp/aboutme.html'


class Dashboard(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = Home.as_view(
            template_name='blogapp/admin_page.html',
        )
        return view(request, *args, **kwargs)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

    def get_object(self):
        object = super(PostDetail, self).get_object()
        object.view_count += 1
        object.save()
        return object
    
    
class CommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blogapp/comment_form.html'
    form_class = CommentForm

    def form_valid(self, form):
        post_id = self.kwargs.get('id')
        post = get_object_or_404(Post, id=post_id)
        self.success_url = f'/blogapp/post/{post.slug}/'
        form.instance.post = post
        return super().form_valid(form)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'author', 'category', 'content', 'images')


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post 
    success_url = reverse_lazy('dashboard')


class PostCategory(LoginRequiredMixin, ListView):
    template_name = 'blogapp/post_category.html'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class NewCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = ('name',)


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article

    def get_object(self):
        object = super(ArticleDetail, self).get_object()
        object.view_count += 1
        object.save()
        return object


class ArticleCat(LoginRequiredMixin, ListView):
    model = Article
    paginate_by = 8
    template_name = 'blogapp/article_category.html'
    

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'content', 'thumbnail')


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'content', 'thumbnail')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('dashboard')

