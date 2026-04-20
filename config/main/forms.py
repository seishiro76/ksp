from django import forms


class ConsultationForm(forms.Form):
    full_name = forms.CharField(
        label="ФИО",
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        label="Электронная почта",
        required=True
    )

    consultation_type = forms.ChoiceField(
        label="Тип консультации",
        choices=[
            ("Очная", "Очная"),
            ("Онлайн", "Онлайн"),
            ("По переписке", "По переписке"),
        ],
        required=True
    )

    urgent = forms.BooleanField(
        label="Срочно нужна консультация",
        required=False
    )

    comment = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False
    )