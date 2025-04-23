from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm

from blog.models import Post

# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('category'):
        posts = posts.filter(category__name=kwargs['category'])
    if kwargs.get('tag'):
        posts = posts.filter(tags__name=kwargs['tag'])
    if kwargs.get('author'):
        posts = posts.filter(author__username=kwargs['author'])

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def single_blog_view(request, pid):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
    
    post = get_object_or_404(Post, id=pid,status=1 ,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save(update_fields=['counted_views'])
    comments=Comment.objects.filter(post=post.id,approved=True)
    form=CommentForm()
    prev_post = Post.objects.filter(status=1 ,published_date__lte=timezone.now(), id__lt=post.id).order_by('id').last()
    next_post = Post.objects.filter(status=1 ,published_date__lte=timezone.now(), id__gt=post.id).order_by('id').first()
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments': comments,
        'form': form,
        
    }
    return render(request, 'blog/single-blog.html', context)