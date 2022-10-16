from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return HttpResponse("<h1> Server is Running About</h1>")


def gallery(request):
    return HttpResponse("<h1> Server is Running Gallery</h1>")


def terms(request):
    return HttpResponse("<h1> Server is Running Terms and Condition</h1>")


def contact(request):
    return HttpResponse("<h1> Server is Running Contact</h1>")


def tour_details(request, id):
    return HttpResponse(f"<h1> Server is Running tour details {id}</h1>")
