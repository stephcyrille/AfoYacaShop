from django.db import models
from django.utils import timezone

from account.models import UserProfile
from checkout.models import Order


class Operation(models.Model):
    trans_ref = models.CharField(max_length=50)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    # initialized, Success, Pending, Failed
    status = models.CharField(max_length=200)
    amount = models.IntegerField()
    buyer_account = models.CharField(max_length=50)
    seller_account = models.CharField(max_length=50)
    vendor = models.CharField(max_length=100)
    trans_date = models.DateTimeField()

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return "Operation: %s" % self.trans_ref