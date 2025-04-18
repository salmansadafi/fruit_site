from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('single_blog/', single_blog_view, name='single_blog'),

]