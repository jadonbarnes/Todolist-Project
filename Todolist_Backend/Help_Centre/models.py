from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Question(models.Model):
    Question = models.CharField(max_length=100,unique=True,null=False)
    Answer = models.CharField(max_length=500,unique=True, null=False)
    position = models.IntegerField(validators=[MaxValueValidator(15)],unique=True,null=False)

    def __str__(self):
        return self.Question

#this is the model for the Guides home page
class Tutorial(models.Model):
    Name = models.CharField(max_length=100,unique=True, null=False)
    Description = models.CharField(max_length=350,unique=True ,null=False)
    Image_Link = models.CharField(max_length=300, null=True)
    Image_Link_High_Res = models.CharField(max_length=300, null=True)
    Difficulty = models.IntegerField(validators=[MaxValueValidator(4)],null=False)

    def __str__(self):
        return self.Name

#this is the linked model for each of the steps in a Tutorial
class Tutorial_Step(models.Model):
    Position = models.IntegerField(null=False)
    Name = models.CharField(max_length=100, null=False)
    Description = models.CharField(max_length=800, null=False)
    Image_Link = models.CharField(max_length=300, null=True)
    Image_Link_High_Res = models.CharField(max_length=300, null=True)
    Tutorial = models.ForeignKey('Tutorial', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
