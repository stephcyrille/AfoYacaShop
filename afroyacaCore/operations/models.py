from django.db import models
from django.utils import timezone

from account.models import UserProfile
from checkout.models import Order

OPERATION_METHOD = (
    ("CASH", "cash"),
    ("ORANGE_MONEY", "orange_money"),
    ("MOMO", "momo"),
    ("VISA", "visa"),
    ("MASTERCARD", "mastercard"),
)
OPERATION_PURPOSE = (
    ("SERVICE", "service"),
    ("PRODUCT", "product"),
    ("REVERSE_PAYMENT", "reverse_payment"),
)


class PaymentOperation(models.Model):
    purpose = models.CharField(max_length=50, choices=OPERATION_PURPOSE, default="")
    value = models.IntegerField(default=0)
    method = models.CharField(max_length=50, choices=OPERATION_METHOD, default="")
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    bayed = models.CharField(max_length=50, default="AYD_ACCOUNT")
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Payment %s - %s" % (self.id, self.purpose)