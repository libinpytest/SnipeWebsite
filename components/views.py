from django.shortcuts import render, redirect, get_object_or_404
from .models import Component
from .forms import ComponentForm

def component_list(request):
    components = Component.objects.all()
    return render(request, 'component_list.html', {'components': components})

def create_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm()
    return render(request, 'create_component.html', {'form': form})

def update_component(request, component_id):
    component = get_object_or_404(Component, pk=component_id)
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES, instance=component)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm(instance=component)
    return render(request, 'update_component.html', {'form': form, 'component': component})

def delete_component(request, component_id):
    component = get_object_or_404(Component, pk=component_id)
    if request.method == 'POST':
        component.delete()
        return redirect('component_list')
    return render(request, 'delete_component.html', {'component': component})
