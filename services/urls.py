from django.urls import path
from services import views

urlpatterns = [
    path("services/", views.services_list, name="services_list"),
    path("services/create/", views.create_services, name="create_services"),
    path("services/update/<int:services_id>/", views.update_services, name="update_services"),
    path("services/delete/<int:services_id>/", views.delete_services, name="delete_services"),
]
