from django.db import models
from django.utils import timezone

from account.models import UserProfile

main_menu_pic_upload_path = "main_menu_nav"
seo_pic_upload_path = "seo"
banner_pic_upload_path = "banner"


class CoreTrackedModel(models.Model):
    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")


class MainMenuNavPicture(CoreTrackedModel):
    clothing = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    shoes = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    bag = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    accessory = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    jewelery = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    lingerie = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    beauty = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)
    editorial = models.FileField(upload_to=main_menu_pic_upload_path, null=True, blank=True)

    def __str__(self):
        return self.pk


class SeoPage(CoreTrackedModel):
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(unique=True)
    keywords = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField()
    url = models.TextField()
    picture = models.FileField(upload_to=seo_pic_upload_path, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.title)


class Banner(CoreTrackedModel):
    name = models.CharField(max_length=250, null=False, blank=False)
    title = models.CharField(max_length=250, null=False, blank=False)
    subTitle = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(unique=True)
    linkText = models.CharField(max_length=250, null=False, blank=False)
    linkUrl = models.TextField()
    active = models.BooleanField(default=False)
    picture = models.FileField(upload_to=banner_pic_upload_path, null=True, blank=True)
    # Let us know if the banner stay on the home page
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.name


