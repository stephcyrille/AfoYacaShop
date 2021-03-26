from django.db import models
from django.utils import timezone

from account.models import UserProfile

OPERATION_METHOD = (
    ("CASH", "cash"),
    ("ORANGE_MONEY", "orange_money"),
    ("MOMO", "momo"),
    ("VISA", "visa"),
    ("MASTERCARD", "mastercard"),
)
OPERATION_PURPOSE = (
    ("SERVICE", "free"),
    ("PRODUCT", "bronze"),
    ("REVERSE_PAYMENT", "reverse_payment"),
)


class PaymentOperation(models.Model):
    purpose = models.CharField(max_length=50, choices=OPERATION_PURPOSE, default="")
    value = models.IntegerField(default=0)
    method = models.CharField(max_length=50, choices=OPERATION_METHOD, default="")
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    bayed = models.CharField(max_length=50, default="AYD_ACCOUNT")
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)

    def __str__(self):
        return "Payment %s - %s" % (self.id, self.purpose)