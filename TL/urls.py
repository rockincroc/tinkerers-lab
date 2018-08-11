"""TL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve 
from  django.conf import settings
import tinkererslab.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',tinkererslab.views.index,name='index'),
    url(r'^wishlist$',tinkererslab.views.wishlist,name='wishlist'),
    url(r'^events$',tinkererslab.views.events,name='events'),
    url(r'^about$',tinkererslab.views.about,name='about'),
    url(r'^gallery$',tinkererslab.views.gallery,name='gallery'),
    url(r'^resources$',tinkererslab.views.resources,name='resources'),
    url(r'^team$',tinkererslab.views.team,name='team'),
    url(r'^feedback$',tinkererslab.views.feedback,name='feedback'),
    url(r'^contact$',tinkererslab.views.contact,name='contact'),
    url(r'^thank$',tinkererslab.views.thank,name='thank'),
    url(r'^static/(?P<path>.*)$', serve,
      {'document_root': settings.STATIC_ROOT}
    ),
]
