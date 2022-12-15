from django.shortcuts import redirect, render, HttpResponse
from .models import Contact, Tour, Gallery
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html')


def gallery(request):
    images = Gallery.objects.all()
    context = {'image': images}
    return render(request, 'home/gallery.html', context)


def terms(request):
    return render(request, 'home/terms.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()

        # Email Variables

    # try:
    #     subject = "New Email From Website"
    #     message = f'Name: {name}, Email: {email}, Phone: {phone}, Messsage: {content}'
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = ['ranjutanti743@gmail.com']
    #     send_mail(subject, message, email_from,
    #               recipient_list, fail_silently=False)
    #     # redirect('/')
    # except Exception as e:
    #     print(e)

    return render(request, 'home/contact.html')


def tour_details(request, id):
    tours = Tour.objects.filter(sno=id)[0]
    context = {'tour': tours}
    return render(request, 'home/details.html', context)
