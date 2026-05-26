from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, RequestForm, DocumentForm
from .models import Client, ConsultationRequest, ConsultationDocument


def consultation_create_view(request):
    success_message = ""

    if request.method == "POST":
        client_form = ClientForm(request.POST)
        request_form = RequestForm(request.POST)
        document_form = DocumentForm(request.POST, request.FILES)

        if client_form.is_valid() and request_form.is_valid() and document_form.is_valid():
            client = client_form.save()

            consultation_request = request_form.save(commit=False)
            consultation_request.client = client
            consultation_request.save()

            document = document_form.save(commit=False)
            document.request = consultation_request
            document.save()

            success_message = "Данные успешно сохранены в базу данных."

            client_form = ClientForm()
            request_form = RequestForm()
            document_form = DocumentForm()
    else:
        client_form = ClientForm()
        request_form = RequestForm()
        document_form = DocumentForm()

    clients = Client.objects.all().order_by("-id")
    requests = ConsultationRequest.objects.filter(removed=False).order_by("-id")
    documents = ConsultationDocument.objects.all().order_by("-id")

    context = {
        "client_form": client_form,
        "request_form": request_form,
        "document_form": document_form,
        "success_message": success_message,
        "clients": clients,
        "requests": requests,
        "documents": documents,
    }

    return render(request, "main/consultation_page.html", context)


def request_list_view(request):
    requests = ConsultationRequest.objects.filter(removed=False).order_by("-id")

    context = {
        "requests": requests,
    }

    return render(request, "main/request_list.html", context)


def request_detail_view(request, pk):
    consultation_request = get_object_or_404(
        ConsultationRequest,
        pk=pk,
        removed=False
    )

    documents = ConsultationDocument.objects.filter(request=consultation_request)

    context = {
        "consultation_request": consultation_request,
        "documents": documents,
    }

    return render(request, "main/request_detail.html", context)


def request_edit_view(request, pk):
    consultation_request = get_object_or_404(
        ConsultationRequest,
        pk=pk,
        removed=False
    )

    client = consultation_request.client

    if request.method == "POST":
        client_form = ClientForm(request.POST, instance=client)
        request_form = RequestForm(request.POST, instance=consultation_request)

        if client_form.is_valid() and request_form.is_valid():
            client_form.save()
            request_form.save()

            return redirect("request_detail", pk=consultation_request.pk)
    else:
        client_form = ClientForm(
            instance=client,
            initial={"confirm_email": client.email}
        )
        request_form = RequestForm(instance=consultation_request)

    context = {
        "client_form": client_form,
        "request_form": request_form,
        "consultation_request": consultation_request,
    }

    return render(request, "main/request_edit.html", context)


def request_remove_view(request, pk):
    consultation_request = get_object_or_404(ConsultationRequest, pk=pk)

    consultation_request.removed = True
    consultation_request.save()

    return redirect("request_list")


def ajax_check_email_view(request):
    email = request.GET.get("email", "")

    email_exists = Client.objects.filter(email=email).exists()

    return JsonResponse({
        "email": email,
        "exists": email_exists,
    })


def ajax_request_detail_view(request, pk):
    consultation_request = get_object_or_404(
        ConsultationRequest,
        pk=pk,
        removed=False
    )

    documents = ConsultationDocument.objects.filter(request=consultation_request)

    document_titles = []

    for document in documents:
        document_titles.append(document.title)

    return JsonResponse({
        "id": consultation_request.id,
        "client": consultation_request.client.full_name,
        "email": consultation_request.client.email,
        "phone": consultation_request.client.phone,
        "consultation_type": consultation_request.consultation_type,
        "urgent": consultation_request.urgent,
        "comment": consultation_request.comment,
        "documents": document_titles,
    })