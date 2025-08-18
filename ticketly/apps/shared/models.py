import uuid
from typing import TYPE_CHECKING, Any

from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

if TYPE_CHECKING:
    pass


class ActiveManager(models.Manager):
    """Manager padrão: ignora registros soft-deletados.

    Usado como `objects`, retorna apenas registros com `deleted_at` nulo.
    """

    def get_queryset(self) -> QuerySet:
        """Retorna queryset filtrando registros excluídos logicamente."""
        return super().get_queryset().filter(deleted_at__isnull=True)


class BaseModel(models.Model):
    """Modelo base para todas as entidades.

    - ID como UUID
    - Timestamps de criação/atualização
    - Soft delete (deleted_at)
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    deleted_at = models.DateTimeField("Deletado em", null=True, blank=True)

    # Managers
    objects = ActiveManager()
    objects_all = models.Manager()

    class Meta:
        """Configurações padrão do modelo base."""

        abstract = True
        ordering = ["-created_at"]

    def delete(
        self, using: Any = None, keep_parents: bool = False
    ) -> tuple[int, dict[str, int]]:
        """Realiza soft delete marcando o campo `deleted_at`.

        Retorna 1 para simular comportamento padrão de delete do Django.
        """
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at", "updated_at"])
        return 1, {"soft_deleted": 1}

    def hard_delete(self, using: Any = None, keep_parents: bool = False) -> None:
        """Remove o registro permanentemente do banco de dados."""
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self) -> None:
        """Restaura um registro previamente soft-deletado."""
        self.deleted_at = None
        self.save(update_fields=["deleted_at", "updated_at"])
