from django import forms
from .models import Client, ConsultationRequest, ConsultationDocument


class ClientForm(forms.ModelForm):
    confirm_email = forms.EmailField(label="Повторите электронную почту")

    class Meta:
        model = Client
        fields = ["full_name", "email", "phone"]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error("confirm_email", "Электронные почты не совпадают.")

        return cleaned_data


class RequestForm(forms.ModelForm):
    agree_rules = forms.BooleanField(
        label="Я подтверждаю правильность введённых данных",
        required=True
    )

    class Meta:
        model = ConsultationRequest
        fields = ["consultation_type", "urgent", "comment"]


class DocumentForm(forms.ModelForm):
    class Meta:
        model = ConsultationDocument
        fields = ["title", "file"]