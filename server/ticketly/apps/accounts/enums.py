from django.db import models


class Roles(models.TextChoices):
    ASSISTANTS = "assistants", "Atendentes"
    TECHNICIAN = "technician", "Técnicos"
