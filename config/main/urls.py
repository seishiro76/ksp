from django.urls import path
from . import views


urlpatterns = [
    path("", views.consultation_create_view, name="consultation_create"),
    path("requests/", views.request_list_view, name="request_list"),
    path("requests/<int:pk>/", views.request_detail_view, name="request_detail"),
    path("requests/<int:pk>/edit/", views.request_edit_view, name="request_edit"),
    path("requests/<int:pk>/remove/", views.request_remove_view, name="request_remove"),

    path("ajax/check-email/", views.ajax_check_email_view, name="ajax_check_email"),
    path("ajax/request/<int:pk>/", views.ajax_request_detail_view, name="ajax_request_detail"),
]