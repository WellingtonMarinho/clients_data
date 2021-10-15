import uuid
import shortuuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modified at'), auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, Unique=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.uuid)

    @property
    def sid(self):
        if not self.uuid:
            return

        instance_uuid = self.uuid
        if type(instance_uuid) == str:
            instance_uuid = uuid.UUID(instance_uuid)

        return shortuuid.encode(instance_uuid)
