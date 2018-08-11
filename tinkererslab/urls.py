from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'$',views.index,name='index'),
    url(r'/wishlist$',views.wishlist,name='wishlist'),
    url(r'/events$',views.events,name='events'),
    url(r'/about$',views.about,name='about'),
    url(r'/gallery$',views.gallery,name='gallery'),
    url(r'/resources$',views.resources,name='resources'),
    url(r'/team$',views.team,name='team'),
    url(r'/feedback$',views.feedback,name='feedback'),
    url(r'/contact$',views.contact,name='contact'),
    url(r'/thank$',views.thank,name='thank'),
]
