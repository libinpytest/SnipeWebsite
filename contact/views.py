from django.shortcuts import render, redirect
from .models import Contact
from .models import Message


# Create your views here.
def contact(request):
    return render(request, 'contact.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        message = request.POST.get('text')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

    return render(request, 'contact.html')

def submit_message(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')

        message_obj = Message(name=name, email=email, message=message, is_new=True)
        message_obj.save()

    return redirect('homeland')
