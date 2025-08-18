from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from apps.shared.models import BaseModel
from .enums import Roles


class User(AbstractUser, BaseModel):
    first_name = None
    last_name = None

    name = CharField(_("Name"), blank=True, max_length=255)
    role = models.CharField(
        _("role"), choices=Roles.choices, default=Roles.ASSISTANTS
    ) 

    class Meta:
        db_table = "users"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
