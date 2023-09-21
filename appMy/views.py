from django.shortcuts import render
from .models import *

# Create your views here.
 

def indexPage(request):
   context = {}
   return render(request, 'index.html', context)

def card_listPage(request, grid=4):
   
   posts = Post.objects.all()
   context = {
      "posts":posts,
      "grid": grid,
   }
   return render(request, 'card_list.html', context)

def detailPage(request, pid):
   post = Post.objects.get(id=pid)
   context = {
       "post": post,
   }
   return render(request, 'detail.html', context)

