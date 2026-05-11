from django.db import models


class Client(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.full_name


class ConsultationRequest(models.Model):
    CONSULTATION_CHOICES = [
        ("Очная", "Очная"),
        ("Онлайн", "Онлайн"),
        ("По переписке", "По переписке"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="Клиент"
    )
    consultation_type = models.CharField(
        "Тип консультации",
        max_length=30,
        choices=CONSULTATION_CHOICES
    )
    urgent = models.BooleanField("Срочно", default=False)
    comment = models.TextField("Комментарий", blank=True)
    removed = models.BooleanField("Удалено", default=False)

    def __str__(self):
        return f"Заявка: {self.client.full_name}"


class ConsultationDocument(models.Model):
    request = models.ForeignKey(
        ConsultationRequest,
        on_delete=models.CASCADE,
        verbose_name="Заявка"
    )
    title = models.CharField("Название документа", max_length=100)
    file = models.FileField("Файл", upload_to="documents/", blank=True, null=True)

    def __str__(self):
        return self.title