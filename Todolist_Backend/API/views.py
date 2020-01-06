# This file determines the data to be sent out by each request

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import bad_request

# this is a local import
from .serializers import *
from .models import *

# this is the ViewSet that tells the API what to do when the request comes in, most of the logic is handled by the ModelViewSet parent class
class ProjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Project.objects.filter(Creator=self.request.user)
    serializer_class = ProjectSerializers
    permission_classes = [permissions.IsAuthenticated]

# this is a custom function that returns the tasks associated with a specific project
    @action(detail = True)
    def Tasks(self, request, pk=None):
        try:
            # this line checks to see if the project is owned by the user
            if Project.objects.get(pk = pk) in Project.objects.filter(Creator=request.user.id):
                data = Task.objects.filter(Project=pk)
                serializer = TaskSerializers(data, many=True)
                return Response(serializer.data)
            else:
                # this returns an error if the user does nto own the project
                return bad_request('Users not authenticated for this request', 400)
        except:
                # this returns a 400 error if there is something wrong with the request
                return bad_request('Error bad request',400)




# this is the ViewSet that tells the API what to do when the request comes in, most of the logic is handled by the ModelViewSet parent class
class TagViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Tag.objects.filter(Creator=self.request.user)
    serializer_class = TagSerializers
    permission_classes = [permissions.IsAuthenticated]


# this is the ViewSet that tells the API what to do when the request comes in, most of the logic is handled by the ModelViewSet parent class
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]

# this is a custom function that returns the children associated with a specific task
    @action(detail=True)
    def Children(self, request, pk=None):
        try:
            data = Task.objects.filter(Parent=pk)
            serializer = TaskSerializers(data, many=True)
            return Response(serializer.data)
        except:
                return bad_request('Error bad request',400)


# this is the ViewSet that tells the API what to do when the request comes in, most of the logic is handled by the ModelViewSet parent class
class FiltersViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Filter.objects.filter(Creator=self.request.user)
    serializer_class = FilterSerializers
    permission_classes = [permissions.IsAuthenticated]

    # this is a custom function that returns the children associated with a specific filter
    @action(detail=True)
    def Filtered_Tasks(self, request, pk=None):
            Local_Filter = Filter.objects.get(pk = pk)
            Command = Local_Filter.Filter()
            Command = eval(Command)
            serializer = TaskSerializers(Command, many=True)
            print(serializer.data)
            try:
                return Response(serializer.data)
            except:
                return bad_request('Error bad request', 400)
