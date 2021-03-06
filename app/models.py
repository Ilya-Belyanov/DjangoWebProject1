"""
Definition of models.
"""

from django.db import models

from datetime import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    video = models.FileField(default = 'temp.mp4', verbose_name='Путь к видео')
    video_1 = models.FileField(default = 'temp.mp4', verbose_name='Путь ко 2 видео')
    video_2 = models.FileField(default = 'temp.mp4', verbose_name='Путь к 3 видео')
    imagevideo = models.FileField(default = 'temp.jpg', verbose_name='Путь к постеру для видео 1')
    imagevideo_1 = models.FileField(default = 'temp.jpg', verbose_name='Путь к постеру для видео 2')
    imagevideo_2 = models.FileField(default = 'temp.jpg', verbose_name='Путь к постеру для видео 3')
    image = models.FileField(default = 'temp.jpg', verbose_name='Путь к картинке')
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    title=models.CharField(max_length=100, unique_for_date="posted", verbose_name='Заголовок')
    description= models.TextField(verbose_name='Краткое содержание')
    content = models.TextField(verbose_name='Полное содержание')
    posted =models.DateTimeField(default=datetime.now(), db_index= True, verbose_name ='Опубликовано')
    
    def get_absolute_url(self):
        '''Возвращает строку с уникальным интернет-адресом записи'''
        return reverse("blogpost", args= [str(self.id)])

    def __str__(self):
        '''Возвращает название'''
        return self.title

    class Meta:
        db_table="Posts" #имя таблицы для модели
        ordering = ["-posted"] #порядок сортирования данных в модели
        verbose_name='статья блога'
        verbose_name_plural='статьи блога'

admin.site.register(Blog)



class Comment(models.Model):
    text=models.TextField(verbose_name='Комментарий')
    data=models.DateTimeField(default=datetime.now(), db_index= True, verbose_name ='Дата')
    author = models.ForeignKey(User, on_delete = models.CASCADE,verbose_name='Автор' )
    post = models.ForeignKey(Blog, on_delete = models.CASCADE,verbose_name='Статья' )   
    

    def __str__(self):
        
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table="Comment" 
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии к статьям блога'

admin.site.register(Comment)
