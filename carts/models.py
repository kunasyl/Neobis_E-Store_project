import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product
from users.models import User


class CartItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_carts',
        verbose_name=_('Товар')
    )
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_carts',
        verbose_name=_('Пользователь')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')