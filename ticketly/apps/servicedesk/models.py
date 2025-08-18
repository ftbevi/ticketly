from django.db import models

from apps.shared.models import BaseModel
from .enums import Priority, Status 


class Ticket(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.LOW)
    sector = models.CharField(max_length=100)
    status = models.CharField(
        max_length=11, choices=Status.choices, default=Status.OPEN)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "tickets"
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
