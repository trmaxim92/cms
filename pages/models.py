from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=400, verbose_name="Заголовок страницы")
    slug = models.SlugField(max_length=400, verbose_name="URL")
    description = models.CharField(max_length=440, verbose_name="Краткое описание страницы")
    body = RichTextField(max_length = 1200, verbose_name = "Текст")
    
    
    def __str__(self):
        return "Страница: {0}".format(self.title)
    
    
    def get_absolute_url(self):
        return reverse("pages:page_view", args=[str(self.slug)])
    
    
    
    
    class Meta:
        verbose_name = "Страницу"
        verbose_name_plural = "Страницы"
    
