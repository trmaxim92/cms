from django.shortcuts import render, get_object_or_404
from .models import Page





def page(requset, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_view.html', {'page':page})

