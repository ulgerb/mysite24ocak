from django.shortcuts import render
from .models import *

# Create your views here.
 

def indexPage(request):
   context = {
      "categorys" : Category.objects.all(),
   }
   return render(request, 'index.html', context)


def card_listPage(request, cate="all", grid=4):

   if cate != "all":
      posts = Post.objects.filter(category__title=cate)
   else:
      posts = Post.objects.all()
   categorys = Category.objects.all()
   context = {
      "posts":posts,
      "cate": cate,
      "grid": grid,
      "categorys": categorys,
   }
   return render(request, 'card_list.html', context)

def detailPage(request, pid): # fnksiyonlar ve sayfalar GET ile çalışırlar
   comments = Comment.objects.filter(post=pid)
   post = Post.objects.get(id=pid)

   if request.method == "POST":
      fullname = request.POST.get("fullname")
      text = request.POST.get("comment")

      comment = Comment(full_name=fullname, text=text, post=post)
      comment.save()
      
   
   context = {
      "comments": comments,
      "post": post,
      "categorys": Category.objects.all(),
   }
   return render(request, 'detail.html', context)

