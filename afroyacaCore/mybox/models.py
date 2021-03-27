from django.db import models
from django.utils import timezone

from products.models import Variety

BOX_STATUS = (
    ("ACTIVATE", "Activate"),
    ("DEACTIVATE", "deactivate"),
)
SUBSCRIPTION_PLAN = (
    ("FREE", "free"),
    ("BRONZE", "bronze"),
    ("SILVER", "silver"),
    ("GOLD", "gold"),
)


class MyBox(models.Model):
    owner = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    total = models.IntegerField(default=0)
    status = models.CharField(choices=BOX_STATUS, default="DEACTIVATE", max_length=30)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)

    def __str__(self):
        return "Box %s" % self.id


class BoxItems(models.Model):
    box = models.ForeignKey(MyBox, on_delete=models.CASCADE, null=True, blank=True)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.IntegerField(default=1)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)

    def __str__(self):
        return "Box %s" % self.id


class BoxSubscriptionPlan(models.Model):
    name = models.CharField(max_length=50, choices=SUBSCRIPTION_PLAN, default="FREE")
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "%s Plan" % self.name
