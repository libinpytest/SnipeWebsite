# from django.shortcuts import render
# from .models import Message
# from django.contrib.auth.decorators import login_required

# def homeland(request):
#     new_message_count = 0
#     greeting = ''

#     if request.user.is_authenticated and request.user.is_superuser:
#         new_message_count = Message.objects.filter(is_new=True).count()
#         greeting = f"Welcome, {request.user.username}!"

#     context = {'new_message_count': new_message_count, 'greeting': greeting}
#     return render(request, 'index.html', context)


# @login_required
# def adminView(request):
#     return render(request, 'index.html')


# def submit_message(request):
#     if request.method == 'POST':
#         name = request.POST.get('Name')
#         email = request.POST.get('Email')
#         message = request.POST.get('Message')

#         message_obj = Message(name=name, email=email, message=message, is_new=True)
#         message_obj.save()

#     return render(request, 'index.html')
