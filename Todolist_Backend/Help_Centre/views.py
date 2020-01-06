from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import *

# Create your views here.
def Help_Centre(request):
    return render(request, 'Help_Centre/Help_Centre.html')

# This is a view for the freqently asked questions page
# This passes all questions to a specific object in the dictionary based on the position value
def FAQ(request):
    context = {  'Question1': Question.objects.get(position=1),
                 'Question2': Question.objects.get(position=2),
                 'Question3': Question.objects.get(position=3),
                 'Question4': Question.objects.get(position=4),
                 'Question5': Question.objects.get(position=5),
                 'Question6': Question.objects.get(position=6),
                 'Question7': Question.objects.get(position=7),
                 'Question8': Question.objects.get(position=8),
                 'Question9': Question.objects.get(position=9),
                 'Question10': Question.objects.get(position=10),
                 'Question11': Question.objects.get(position=11),
                 'Question12': Question.objects.get(position=12),
                 'Question13': Question.objects.get(position=13),
                 'Question14': Question.objects.get(position=14),
                 'Question15': Question.objects.get(position=15)
                 }
    return render(request, 'Help_Centre/Frequently_Asked_Questions___1.html', context)

#The guide pages is the home page for the tutotrials, it passes the Tutorial home object through
def Guides(request):
    context = { 'Tutorials': Tutorial.objects.order_by('Difficulty')}
    return render(request, 'Help_Centre/Guides___1.html',context)

#The Guides_Sub_Page passes the tutorial object and steps through
def Guides_Sub_Pages(request, Tutorial_PK):
    Tutorial_Steps = Tutorial_Step.objects.filter(Tutorial=Tutorial_PK).order_by('Position')
    Tutorial_Main = Tutorial.objects.get(pk = Tutorial_PK)
    context = {'steps':Tutorial_Steps,
               'tutorial':Tutorial_Main}
    return render(request, 'Help_Centre/tutorial_page___1.html',context)
