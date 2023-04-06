from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField




class Category(models.Model):
    name = models.CharField(max_length=600, verbose_name="Название категории")
    slug = models.SlugField(max_length=600, verbose_name="URL")
    
    def __str__(self):
        return "Категория: {0}".format(self.name)
    
    
    def get_absolute_url(self):
        return reverse("blog:category_view", args=[str(self.slug)])
    
    
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
        
class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
    
    
class Article(models.Model):
    
    STATUS_PUBLISHED = (
        ('draft', 'Черновик'),
        ('published', 'Публикация'),
    )
    
    title = models.CharField(max_length=440, verbose_name="Заголовок")
    slug = models.SlugField(max_length=440, verbose_name="URL")
    img = models.ImageField(upload_to = 'media/article', blank=True, null=True, verbose_name="Изображение")
    body = RichTextField(max_length=4000, verbose_name="Текст")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=12, choices=STATUS_PUBLISHED, verbose_name="Статус публикации")
    
    published = PublishedArticleManager()
    
    def get_absolute_url(self):
        return reverse('blog:article_view', args=[self.published_at.year, self.published_at.month, self.published_at.day, str(self.slug)])
    
    def __str__(self):
        return "Запись {0}".format(self.title)
    
    class Meta:
        ordering = ('-published_at',)
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
    
    