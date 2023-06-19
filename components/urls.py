from django.urls import path
from components import views

urlpatterns = [
    path('components/', views.component_list, name='component_list'),
    path('create/components', views.create_component, name='create_component'),
    path('update/<int:component_id>/components', views.update_component, name='update_component'),
    path('delete/<int:component_id>/components', views.delete_component, name='delete_component'),
]
