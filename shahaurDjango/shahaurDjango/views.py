from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("HEllo,sher Welcome to django homepage")

    # return render(request,'index.html')
    # return render(request,'website/index.html')


def contact(request):
    return HttpResponse("HEllo,sher Welcome to django contact")



def about(request):
    # return HttpResponse("HEllo,sher Welcome to django About")
    return render(request,'website/About.html')