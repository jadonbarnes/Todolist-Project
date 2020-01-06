# this is not a standard Django file
# this file is unique to the django rest framework
# this converts models into JSON format to be sent out

from rest_framework import serializers
from .models import *

# this is the serializer for the project model - we import a Parent Serializer that handles most of the logic
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        # this is the model that the serializer will reference for information
        model = Project
        # this means the Project model uses all the fields in the model
        fields = '__all__'

# this is the serializer for the Tag model - we import a Parent Serializer that handles most of the logic
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        # this is the model that the serializer will reference for information
        model = Tag
        # this means the Project model uses all the fields in the model
        fields = '__all__'

# this is the serializer for the Task model - we import a Parent Serializer that handles most of the logic
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        # this is the model that the serializer will reference for information
        model = Task
        # this means the Project model uses all the fields in the model
        fields = '__all__'

# this is the serializer for the Filter model - we import a Parent Serializer that handles most of the logic
class FilterSerializers(serializers.ModelSerializer):
    class Meta:
        # this is the model that the serializer will reference for information
        model = Filter
        # this means the Project model uses all the fields in the model
        fields = '__all__'
