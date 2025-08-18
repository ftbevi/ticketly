from django.db import models


class Priority(models.TextChoices):
    LOW = "low", "Baixa"
    MEDIUM = "medium", "Em andamento"
    HIGH = "high", "Concluído"


class Status(models.TextChoices):
    OPEN = "open", "Atendentes"
    INPROGRESS = "in_progress", "Técnicos"
    COMPLETED = "completed", "Completos"
