from django.db import models
from django.utils import timezone

from account.models import UserProfile
from products.models import Variety

BOX_STATUS = (
    ("ACTIVATE", "Activate"),
    ("DEACTIVATE", "deactivate"),
)


class MyBox(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
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