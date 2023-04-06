from django.urls import path
from .views import page

app_name = 'pages'

urlpatterns = [
    path('<slug:slug>/', page, name = "page_view"),
]
