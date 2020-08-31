from django.shortcuts import get_object_or_404, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Category, Article
from .forms import PostForm

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_cat'))
    

class Home(ListView):
    model = Post
    template_name = 'blogapp/home.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-pub_date')[:6]
        context['articles'] = Article.objects.order_by('-timestamp')[:6]
        return context


@method_decorator(login_required, name='dispatch') 
class About(TemplateView):
    template_name = 'blogapp/aboutme.html'


@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        view = Home.as_view(
            template_name='blogapp/admin_page.html',
        )
        return view(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model = Post

    def get_object(self):
        object = super(PostDetail, self).get_object()
        object.view_count += 1
        object.save()
        return object
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comments'] = Comment.objects.filter(post=self.get_object())    
    #     context['form'] = CommentForm
    #     return context

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'author', 'category', 'content', 'images')

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post 
    success_url = reverse_lazy('dashboard')

@method_decorator(login_required, name='dispatch')
class PostCategory(ListView):
    template_name = 'blogapp/post_category.html'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

@method_decorator(login_required, name='dispatch')
class NewCategory(CreateView):
    model = Category
    fields = ('name',)

@method_decorator(login_required, name='dispatch')
class ArticleDetail(DetailView):
    model = Article

    def get_object(self):
        object = super(ArticleDetail, self).get_object()
        object.view_count += 1
        object.save()
        return object

@method_decorator(login_required, name='dispatch')
class ArticleCat(ListView):
    model = Article
    paginate_by = 8
    template_name = 'blogapp/article_category.html'
    
@method_decorator(login_required, name='dispatch')
class ArticleCreate(CreateView):
    model = Article
    fields = ('title', 'content', 'thumbnail')

@method_decorator(login_required, name='dispatch')
class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title', 'content', 'thumbnail')

@method_decorator(login_required, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('dashboard')

