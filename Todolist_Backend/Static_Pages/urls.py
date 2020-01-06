from django.urls import path

from . import views

urlpatterns = [
    #Home page with domain/
    path('', views.home, name='home'),
    #menu page with domain/menu
    path('menu',views.menu, name='menu'),
    #menu page with domain/features
    path('features',views.features,name='features')
]
