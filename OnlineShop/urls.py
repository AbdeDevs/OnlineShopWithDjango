from django.urls import path, include

from OnlineShop.views import home, services, shop, blog, contact

urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),

]