from django.shortcuts import render
from blog.models import Post
from .models import Product,Team
from .forms import contactForm,subscribe
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully.')
        else:
            messages.error(request, 'Message not sent.')
    form = contactForm()
    return render(request, 'core/contact.html', {'form': form})

def notfound_view(request):
    return render(request, 'core/404.html', status=404)

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

def subscribe_view(request):
    if request.method == 'POST':
        form = subscribe(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed successfully.')
        else:
            messages.error(request, 'Not subscribed.')
    return HttpResponseRedirect('/')



# Create your views here.
