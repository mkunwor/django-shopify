
from django.urls import path,include
from shop import views


urlpatterns = [
    path('',views.shop, name='shop'),
        path('home',views.home, name='home')

]