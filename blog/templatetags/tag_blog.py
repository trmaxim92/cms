from django import template
from blog.models import Article, Category

register = template.Library()


@register.simple_tag
def total_articles():
    return Article.published.count()



@register.simple_tag
def category():
    categories =  Category.objects.all()
    return {'categories':categories}