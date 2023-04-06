from django.urls import path
from .views import article_list, article_view, category_view

app_name = 'blog'

urlpatterns = [
    path('', article_list, name= "article_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', article_view, name = "article_view"),
    path('<slug:slug>/', category_view, name = "category_view"),
]
