from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Category, Article


def article_list(request):
    
    object_list = Article.published.all()
    
    paginator = Paginator(object_list, 10)
    
    page = request.GET.get('page')
    
    try:
        
        articles = paginator.page(page)
        
    except PageNotAnInteger:
        
        articles = paginator.page(1)
        
    except EmptyPage:
        
        articles = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/article/article_list.html', {'articles':articles, 'page':page})
        

def article_view(request, year, month, day, slug):
    
    article = get_object_or_404(Article, 
                                slug=slug,
                                status ='published',
                                published_at__year = year,
                                published_at__month = month,
                                published_at__day = day)
    
    return render(request, 'blog/article/article_view.html', {'article':article})


def category_view(request, slug):
    
    category = Category.objects.select_related().get(slug=slug)
    
    articles = category.article_set.all()
    
    return render(request, 'blog/category/category_view.html', {'category':category, 
                                                                'articles':articles}) 




def article_search(request):
    pass