from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog.html')

def single_blog_view(request):
    return render(request, 'blog/single-blog.html')