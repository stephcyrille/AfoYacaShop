from django.db import models
from django.utils import timezone

from account.models import UserProfile
from cart.models import Cart
from account.models import Contact


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    # initialized, Pending, delivered, canceled
    status = models.CharField(max_length=200)
    sub_total = models.IntegerField()
    tax_total = models.IntegerField(default=0)
    delivery_fees = models.IntegerField(default=0)
    final_total = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=200)
    express_delivery = models.BooleanField(default=False)
    delivery_date = models.DateTimeField(null=True, blank=True)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return "Order: %s" % self.id