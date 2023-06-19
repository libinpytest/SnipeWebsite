from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServicesForm

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services_list.html', {'services': services})

def create_services(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServicesForm()
    return render(request, 'create_services.html', {'form': form})

def update_services(request, services_id):
    services = get_object_or_404(Service, pk=services_id)
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES, instance=services)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServicesForm(instance=services)
    return render(request, 'update_services.html', {'form': form, 'services': services})

def delete_services(request, services_id):
    services = get_object_or_404(Service, pk=services_id)
    if request.method == 'POST':
        services.delete()
        return redirect('services_list')
    return render(request, 'delete_services.html', {'services': services})
