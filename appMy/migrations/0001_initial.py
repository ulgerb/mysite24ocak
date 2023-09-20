# Generated by Django 4.2.5 on 2023-09-19 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori Başlığı')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Alt Başlık')),
                ('text', models.TextField(verbose_name='İçerik')),
                ('date_now', models.DateField(auto_now_add=True, verbose_name='Tarih')),
                ('author', models.CharField(max_length=50, verbose_name='Yazar')),
                ('image', models.FileField(upload_to='post', verbose_name='Resim')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMy.category', verbose_name='Kategori')),
            ],
        ),
    ]
