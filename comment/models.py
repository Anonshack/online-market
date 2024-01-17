from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from store.models import Product

class Comment(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'
