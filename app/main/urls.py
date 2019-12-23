from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/sent', views.contact_sent, name='contact_sent'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
]
