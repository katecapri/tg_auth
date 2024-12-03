import uuid
import logging
from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger('app')


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=125, verbose_name=_("Имя пользователя"))
    token = models.CharField(max_length=125, verbose_name=_("Токен пользователя"))
    chat_id = models.IntegerField(verbose_name=_("ID чата"))

    class Meta:
        app_label = 'link'
        db_table = 'users'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.name