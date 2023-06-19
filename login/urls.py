from django.urls import path
from .views import login_view, profile_view

urlpatterns = [
    # other URL patterns
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    # other URL patterns
]
