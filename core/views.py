from django.shortcuts import render

def index_view(request):
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def notfound_view(request):
    return render(request, 'core/404.html')




# Create your views here.
