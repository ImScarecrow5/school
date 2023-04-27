from django.db import models
from django.urls import reverse

class School(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержимое статьи')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_publised = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time', 'title']