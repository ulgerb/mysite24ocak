from django.db import models

# Create your models here.

 
class Category(models.Model):
   title = models.CharField(("Kategori Başlığı"), max_length=50)
   
   def __str__(self) -> str:
      return self.title

class Post(models.Model):
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   subtitle = models.CharField(("Alt Başlık"), max_length=50)
   text = models.TextField(("İçerik"))
   date_now = models.DateField(("Tarih"), auto_now_add=True)
   author = models.CharField(("Yazar"), max_length=50)
   image = models.FileField(("Resim"), upload_to="post", max_length=100)
   
   def __str__(self) -> str:
      return self.title


