from django.shortcuts import render

# Create your views here.
def even(request):
    return render(request,"even.html")