from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        verbose_name = 'کابر'
        verbose_name_plural = 'کاربران'
    
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام') 
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام خانوادگی') 
    phone_number = models.CharField(max_length=11, unique=True, blank=True, null=True, verbose_name='شماره تلفن')

    def __str__(self):
        return self.username 

class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    name = models.CharField(max_length=250, verbose_name='نام دسته بندی')

    def __str__(self):
        return self.name 
    
class Article(models.Model):
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات' 
    
    class Status(models.TextChoices):
        PUBLISH = "منتشر شده","publish"
        REJECT = "تایید نشده", "reject"
        PENDING = "در انتشار تایید", "pending"

    title = models.CharField(max_length=255, verbose_name='تیتر')
    description = models.TextField(null=True, verbose_name='توضیحات')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default='ناشناس', verbose_name='نویسنده')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    time_update = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, verbose_name='وضعیت')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    

class Comment(models.Model):
    class Meta:
        verbose_name = 'نظر '
        verbose_name_plural = 'نظرات'
    
    class Status(models.TextChoices):
        PUBLISH = "منتشر شده","publish"
        REJECT = "تایید نشده", "reject"
        PENDING = "در انتشار تایید", "pending"
    
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    time_update = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default='unknown', verbose_name='نویسنده')
    content = models.ForeignKey(to=Article, on_delete=models.SET_NULL, null=True, verbose_name='محتوا')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, verbose_name='وضعیت')
    comment = models.TextField(verbose_name='نظر')

    def __str__(self):
        return f"{self.user.username}::{self.comment[:8:1]}"
    
class MultiMedia(models.Model):
    class Meta:
        verbose_name = " محتوای چندرسانه ای"
        verbose_name_plural = "محتواهای چند رسانه ای"

    time_created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    time_update = models.DateTimeField(auto_now=True, verbose_name="زمان ویرایش")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="مقاله", related_name='files')
    file = models.FileField(upload_to="./blog", verbose_name="فایل")

    def __str__(self):
        return f"{self.id} :: {self.article.title}"