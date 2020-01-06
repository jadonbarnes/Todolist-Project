from django.urls import path

from . import views

urlpatterns = [
    # help center (Misspelled name of center it is always centre)
    path('Help_Centre', views.Help_Centre, name='help_centre'),
    # this is the freqently asked questions
    path('Frequently_Asked_Questions',views.FAQ, name='frequently asked questions'),
    # This is the home page for the Guides section
    path('Guides',views.Guides,name='guides'),
    # This is dynamic meaning it takes an int from that url and compares it to Tutorial primary keys
    path('<int:Tutorial_PK>',views.Guides_Sub_Pages, name='guides sub pages')

]
