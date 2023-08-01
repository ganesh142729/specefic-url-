from django.shortcuts import render

# Create your views here.
def prime (request):
    return render(request,"prime.html")