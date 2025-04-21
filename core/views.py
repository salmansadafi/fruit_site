from django.shortcuts import render
from blog.models import Post
from .models import Product,Team
from django.utils import timezone
from django.shortcuts import get_object_or_404

def index_view(request,**kwargs):
    posts=Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')[:3]
    if kwargs.get('category'):
        posts = posts.filter(category__name=kwargs['category'])
    products=Product.objects.all()
    context = {
        'posts': posts,
        'products': products
    }
    
    return render(request, 'core/index.html',context)

def about_view(request):
    teams=Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'core/about.html',context)

def contact_view(request):
    return render(request, 'core/contact.html')

def notfound_view(request):
    return render(request, 'core/404.html')

def cart_view(request):
    return render(request, 'core/cart.html')

def checkout_view(request):
    return render(request, 'core/checkout.html')

def shop_view(request):
    return render(request, 'core/shop.html')

def single_product_view(request,pid):
    product=get_object_or_404(Product,id=pid)
    related_products=Product.objects.filter(category__in=product.category.all()).exclude(id=product.id)[:3]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'core/single-product.html',context)




# Create your views here.
