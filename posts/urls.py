from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.list_posts, name='posts'),
    path('create/', views.create_post_view, name='create_post'),
    path('<int:post_id>/update', views.update_post_view, name='update_post'),
    path('<int:post_id>/delete', views.delete_post_view, name='delete_post'),
    path('<int:post_id>', views.view_post_detail, name='view_post_detail'),
]
