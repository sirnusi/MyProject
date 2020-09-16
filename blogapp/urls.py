from django.urls import path
from blogapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post/comments/<int:id>/', views.CommentView.as_view(), name='new_comment'),
    path('article/like/<int:id>/', views.LikeView, name='like_post'),
    path('category/new/', views.NewCategory.as_view(), name='new_cat'),
    path('article/<slug:slug>/delete/', views.ArticleDelete.as_view(), name='article_delete'),
    path('article/<slug:slug>/update/', views.ArticleUpdate.as_view(), name='article_update'), 
    path('article/new/', views.ArticleCreate.as_view(), name='article_new'),
    path('article/cat/', views.ArticleCat.as_view(), name='article_cat'),
    path('article/<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('about/', views.About.as_view(), name='about'),
    path('category/<category>/', views.PostCategory.as_view(), name='post_by_category'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='blogapp/login.html'), name='login'),
    path('post/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<slug:slug>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('post/new/', views.PostCreate.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.Home.as_view(), name='home'),
]
