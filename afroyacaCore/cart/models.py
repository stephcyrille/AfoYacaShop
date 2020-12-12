import uuid
from django.db import models
from django.utils import timezone

from account.models import UserProfile
from products.models import Variety


class Cart(models.Model):
    ref = models.CharField(max_length=10, null=True, blank=True)
    total = models.IntegerField(default=0)
    status = models.CharField(max_length=25, default='Open')  # Open, Canceled, close

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return "Cart n° %s" % self.ref

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.ref = str(uuid.uuid4()).split('-')[0]
        return super(Cart, self).save(*args, **kwargs)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.IntegerField(default=1)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return 'Cart %s - %s (%s)' % (str(self.cart.ref), self.variety.product.title, self.variety.color.title)

