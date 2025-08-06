from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Homepage")

def about(request):
    context={
        "age": 20,
        "name":"Samriddha"}
    return render(request, "pages/about.html",context)
