"""Todolist_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #admin pages
    path('admin/', admin.site.urls),
    #static pages and home page
    path('',include('Static_Pages.urls')),
    #help center
    path('help/', include('Help_Centre.urls')),
    #authentication
    path('accounts/',include('django.contrib.auth.urls')),
    # API paths (these are handled in the same way as usual however the API urls file uses a dynamic router)
    path('API/',include('API.urls'))
]
