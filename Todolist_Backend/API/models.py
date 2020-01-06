from django.db import models
from django.contrib.auth.models import User

import re
import datetime

class Task(models.Model):
    #Fixed fields
    Name = models.CharField(max_length=100)
    Content = models.TextField(blank=True, null=True)
    Notes = models.TextField(blank=True, null=True)
    Due_Date = models.DateField(blank=True, null=True)

    # These are choice field they allow the user to pick from any of the items listed in the choices list
    Priority = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
    )
    Priority = models.CharField(max_length=1, choices=Priority,null=True, blank=True)

    # this is the list that represents the system tags, this can be updated at any time (even without reloding the server)
    System_Tags = (
        ('heading','heading'),
        ('parent','parent')
    )
    System_Tags = models.CharField(max_length=30, choices=System_Tags, null=True, blank=True)

    #links to foreign objects
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    Project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)
    Tags = models.ManyToManyField('Tag', blank=True)
    Creator = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.Name




class Project(models.Model):
    #Fixed fields
    Name = models.CharField(max_length=100)

    #relationships
    Creator = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    Tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.Name

class Tag(models.Model):
    #Fixed fields
    Name = models.CharField(max_length=100)

    #relationships
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Name

class Filter(models.Model):
    #Fixed fields
    Name = models.CharField(max_length=100)
    Filter_Command = models.TextField()

    #relationships
    Creator = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.Name

    def Filter(self):
        Command = self.Filter_Command
        Command = re.split('([|&])', Command)
        print(Command)
        for Position in range(0, len(Command)):
            if "(" in Command[Position]:
                Command[Position] = Command[Position].replace('(', "", 1)
                Command[Position] = Command[Position].replace(')', "", 1)
                Command[Position] = Filter(Command[Position])
            if Command[Position] != '|' or '&':
                Function = 'filter'
                if "!" in Command[Position]:
                    Command[Position] = Command[Position].replace('!', "", 1)
                    Function = 'exclude'
                if "P:" in Command[Position]:
                    Command[Position] = Command[Position].replace('P:', "", 1)
                    Command[Position] = "Task.objects." + Function + "(Priority = " + Command[Position] + ")"
                elif "@" in Command[Position]:
                    Command[Position] = Command[Position].replace('@', "", 1)
                    Tag_Primary_Key = Tag.objects.get(Name=Command[Position])
                    Command[Position] = "Task.objects." + Function + "(Tags = " + Tag_Primary_Key + ")"
                elif "#" in Command[Position]:
                    Command[Position] = Command[Position].replace('#', "", 1)
                    Project_Primary_Key = Project.objects.get(Name=Command[Position])
                    Command[Position] = "Task.objects." + Function + "(Project = " + Project_Primary_Key + ")"
                elif "Today" in Command[Position]:
                    Command[Position] = "Task.objects." + Function + "(Due_Date = datetime.date.today())"
                elif "After:" in Command[Position]:
                    Command[Position] = Command[Position].replace('After:', "", 1)
                    Command[Position] = "Task.objects." + Function + "(Due_Date__gte = " + Command[Position] + ")"
                elif "Before:" in Command[Position]:
                    Command[Position] = Command[Position].replace('Before:', "", 1)
                    Command[Position] = "Task.objects." + Function + "(Due_Date__lte = " + Command[Position] + ")"
        Command.append("&")
        Command.append("Task.objects.filter(Creator = request.user.id)")
        Command = ''.join(Command)
        return Command
