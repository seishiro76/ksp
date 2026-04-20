from django.urls import path
from .views import consultation_create_view

urlpatterns = [
    path("", consultation_create_view, name="consultation_create"),
]