from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('HOME')
    return render(request, 'OnlineShop/home.html')

def services(request):
    #return HttpResponse('SERVICES')
    return render(request, 'OnlineShop/services.html')

def shop(request):
    #return HttpResponse('SHOP')
    return render(request, 'OnlineShop/shop.html')

def blog(request):
    #return HttpResponse('BLOG')
    return render(request, 'OnlineShop/blog.html')


def contact(request):
    #return HttpResponse('CONTACT')
    return render(request, 'OnlineShop/contact.html')