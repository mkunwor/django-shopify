from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def shop(request):
   return render(request, 'shop/shop_nav.html')

def home(request):
   return render(request,'shop/index.html')