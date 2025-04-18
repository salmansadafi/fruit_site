from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404

from blog.models import Post

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')
    
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def single_blog_view(request, pid):
    post = get_object_or_404(Post, id=pid,status=1 ,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save(update_fields=['counted_views'])
    prev_post = Post.objects.filter(status=1 ,published_date__lte=timezone.now(), id__lt=pid).order_by('id').first()
    next_post = Post.objects.filter(status=1 ,published_date__lte=timezone.now(), id__gt=pid).order_by('id').last()
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        
    }
    return render(request, 'blog/single-blog.html', context)