import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from products.models import Product


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_id = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_orders',
        verbose_name=_('Пользователь')
    )
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_orders',
        verbose_name=_('Товар')
    )
    product_count = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')



