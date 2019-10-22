from django.urls import path, re_path
from . import views

from django.views.generic.base import TemplateView


app_name = 'books'

urlpatterns = [
    path('', TemplateView.as_view(template_name="detail_book.html"), name='detail'),
]
