from django.urls import path
from blog.views import *
from .feeds import RssTutorialsFeeds

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<int:pid>', single_blog_view, name='single_blog'),
    path('category/<str:category>', blog_view, name='category'),
    path('tag/<str:tag>', blog_view, name='tag'),
    path('author/<str:author>', blog_view, name='author'),
    path('search/', search_view, name='search'),
    path('rss/feed', RssTutorialsFeeds(), name="tutorial_feed"),
    

]