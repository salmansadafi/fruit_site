from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm
from django.contrib import messages
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('category'):
        posts = posts.filter(category__name=kwargs['category'])
    if kwargs.get('tag'):
        posts = posts.filter(tags__name=kwargs['tag'])
    if kwargs.get('author'):
        posts = posts.filter(author__username=kwargs['author'])

    page_number = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def single_blog_view(request, pid):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment added successfully.')
        else:
            messages.error(request, 'Comment not added.')
    
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

def search_view(request):
    posts=Post.objects.filter(status=1 ,published_date__lte=timezone.now())
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(title__contains=s)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
