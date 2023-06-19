from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def homeland(request):
    new_message_count = 0
    greeting = ''

    if request.user.is_authenticated:
        if request.user.is_superuser:
            session = SessionStore(session_key=request.session.session_key)
            new_message_count = Message.objects.filter(is_new=True).count()
            greeting = f"Welcome, {request.user.username}!"

            # Store the new message count in the session
            session['new_message_count'] = new_message_count
            session.save()
        else:
            # Retrieve the new message count from the session
            session = SessionStore(session_key=request.session.session_key)
            new_message_count = session.get('new_message_count', 0)

    context = {'new_message_count': new_message_count, 'greeting': greeting}

    if new_message_count > 0 and request.user.is_superuser:
        context['notification_url'] = '/notifications/'  # Modify the URL as needed

    return render(request, 'index.html', context)


@login_required
def adminView(request):
    messages = Message.objects.all()
    return render(request, 'notification.html', {'messages': messages})


def submit_message(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')

        message_obj = Message(name=name, email=email, message=message, is_new=True)
        message_obj.save()

    return redirect('homeland')


@login_required
def notifications(request):
    # Retrieve the new message count for the authenticated user
    new_message_count = Message.objects.filter(is_new=True).count()

    # Mark all the user's messages as read (not new)
    Message.objects.filter(is_new=True).update(is_new=False)

    # Retrieve the messages for the authenticated user
    messages = Message.objects.all()

    context = {
        'messages': messages,
        'new_message_count': new_message_count,
    }
    return render(request, 'notifications.html', context)


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        # Delete the message
        message.delete()
        return redirect('notifications')
    return redirect('homeland')


@login_required
def reset_message_count(request):
    if request.method == 'POST':
        # Reset the message count for the authenticated user
        Message.objects.filter(is_new=True).update(is_new=False)

        return JsonResponse({'status': 'success'})
    else:
        # Handle the case if the view is accessed with GET or other HTTP methods
        return JsonResponse({'status': 'error'})


def logout_view(request):
    logout(request)
    return redirect('homeland')
