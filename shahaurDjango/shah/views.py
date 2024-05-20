from django.shortcuts import render

# Create your views here.
def all_items(request):
    return render(request,'shah/all_items.html')