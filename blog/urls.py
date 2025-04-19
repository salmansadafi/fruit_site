from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<int:pid>', single_blog_view, name='single_blog'),
    path('category/<str:category>', blog_view, name='category'),
    path('tag/<str:tag>', blog_view, name='tag'),
    path('author/<str:author>', blog_view, name='author'),
    

]