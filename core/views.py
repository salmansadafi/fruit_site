from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def index_view(request):
    posts=Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')[:3]
    context = {
        'posts': posts
    }
    
    return render(request, 'core/index.html',context)

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def notfound_view(request):
    return render(request, 'core/404.html')




# Create your views here.
