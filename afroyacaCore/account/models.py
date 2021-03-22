from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    gender = models.CharField(max_length=10, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=False, related_name="userprofile", on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(null=True, blank=True, max_length=100)
    address = models.CharField(null=True, blank=True, max_length=250, default='')
    birth_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()


class Contact(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200)
    address_precision = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # One user can have many addresses but he must choose a specific by default
    main = models.BooleanField(default=False)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return "Contact: %s %s" % (self.profile.first_name, self.profile.last_name)
