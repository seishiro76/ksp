from django.shortcuts import render
from .forms import ConsultationForm


def consultation_view(request):
    submitted_data = None

    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
    else:
        form = ConsultationForm()

    return render(request, "main/form_page.html", {
        "form": form,
        "submitted_data": submitted_data,
    })