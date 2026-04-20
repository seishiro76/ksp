from django.shortcuts import render
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
    requests = ConsultationRequest.objects.all().order_by("-id")
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