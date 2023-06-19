from django.urls import path
from products import views

urlpatterns = [
    path("products/", views.products_list, name="products_list"),
    path("create/products", views.create_products, name="create_products"),
    path("update/<int:products_id>", views.update_products, name="update_products"),
    path("delete/<int:products_id>", views.delete_products, name="delete_products"),
]
