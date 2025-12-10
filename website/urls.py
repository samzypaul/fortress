from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path("", views.home, name='home'),
    path("services/",views.services, name='services'),
    path("experience",views.experience, name='experience'),
    path("about/",views.about, name='about'),
    path("quotation/",views.quotation, name='quotation'),
    path("get_quote/",views.get_quote, name='get_quote'),
]