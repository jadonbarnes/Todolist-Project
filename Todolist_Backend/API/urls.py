# This file determines dynamically the url paths for each view in the views file.

from django.urls import path, include
from . import views
from rest_framework import routers

# this sets the DefualtRotuer object equal to router, this object handles the generation of the URLs
router = routers.DefaultRouter()

# here we register the VieSet's created to the router
router.register('project',views.ProjectViewSet,basename='project')
router.register('tag',views.TagViewSet,basename='tag')
router.register('task',views.TaskViewSet,basename='task')
router.register('filter',views.FiltersViewSet, basename='filter')


urlpatterns = [
    # router.urls is a summary of the data the router object produces in the form of that django can interpret
    path('',include(router.urls))

]
