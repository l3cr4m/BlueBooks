from django.urls import path, re_path
from . import views

from django.views.generic.base import TemplateView


app_name = 'profil'

urlpatterns = [
    path('sign_in', TemplateView.as_view(template_name="sign_in.html"), name='sign_in'),
    path('sign_up', TemplateView.as_view(template_name="sign_up.html"), name='sign_up'),
]
