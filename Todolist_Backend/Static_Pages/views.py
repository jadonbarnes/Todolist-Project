from django.shortcuts import render

# Create your views here.

#Home page - static file hosted in cloud, HTML + CSS + Javascript in line
def home(request):
    #no data passed to render + dynamic links
    return render(request, 'Static_Pages/Home_Page__3_.html')

#Menu page - static file hosted in cloud, HTML + CSS + Javascript in line
def menu(request):
    # no data passed to render + dynamic links
    return render(request, 'Static_Pages/Menu.html')

#Features pages - static file hosted in cloud, HTML + CSS + Javascript in line
def features(request):
    # no data passed to render + dynamic links
    return render(request,'Static_Pages/Features.html')
