from django.urls import path
from .views import consultation_view

urlpatterns = [
    path("", consultation_view, name="consultation"),
]