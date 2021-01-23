import random
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from account.models import UserProfile

catalog_upload_path = "catalogs"
category_upload_path = "categories"
collection_upload_path = "collections"
color_motif_upload_path = "motifs"


def product_variety_image_path(instance, filename):
    category = instance.product.category.title
    category_slug = slugify(category)
    return "products/%s/variety/%s" % (category_slug, instance.product.slug)


class Catalog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    picture = models.FileField(upload_to=catalog_upload_path, null=True)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_catalog", kwargs={"slug": self.slug})


class Collection(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    picture = models.FileField(upload_to=collection_upload_path, null=True)
    # This help to know if the collection will be present on the home page, beside mag home cover
    is_home = models.BooleanField(default=False)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_collection", kwargs={"slug": self.slug})


# Clothing, Bag, Jewel, Accessory, etc.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    picture = models.FileField(upload_to=category_upload_path, null=True)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_category", kwargs={"slug": self.slug})

    def get_single_picture(self):
        """
        Get only one picture
        """
        return self.picture.url


# Dress, skirt, Polo, shirt, Jeans, etc.
class Group(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_group", kwargs={"slug": self.slug})


class Product(models.Model):
    ref = models.CharField(max_length=12)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    description = models.TextField(default='')
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(Group, blank=False, null=True, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, blank=True, null=True, on_delete=models.CASCADE)
    material = models.CharField(max_length=150, null=True, blank=True)  # Material in which the product is made
    is_feature = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    flash_sale = models.BooleanField(default=False)
    # TODO Set currency field here, then create method field for returning price in a specific currency

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})

    def get_pictures(self):
        """
        Get max 4 pictures
        """
        pics = []
        # si le queryset services_of_pack est grand
        v = Variety.objects.filter(product=self).first()

        if v is not None:
            if v.picture1:
                pics.append(v.picture1.url)
            if v.picture2:
                pics.append(v.picture2.url)
            if v.picture3:
                pics.append(v.picture3.url)
            if v.picture4:
                pics.append(v.picture4.url)

        return pics

    def get_single_picture(self):
        """
        Get only one picture
        """
        pictures = self.get_pictures()
        pic = random.choice(pictures)
        return pic


class Color(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    picture = models.FileField(upload_to=color_motif_upload_path, null=True)

    def __str__(self):
        return self.title


class Variety(models.Model):
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE, related_name="product_variety")
    color = models.ForeignKey(Color, blank=True, null=True, on_delete=models.CASCADE)
    size = models.ForeignKey("Size", blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    picture1 = models.FileField(upload_to=product_variety_image_path, null=True, blank=True)
    picture2 = models.FileField(upload_to=product_variety_image_path, null=True, blank=True)
    picture3 = models.FileField(upload_to=product_variety_image_path, null=True, blank=True)
    picture4 = models.FileField(upload_to=product_variety_image_path, null=True, blank=True)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return '%s - %s' % (self.product.title, self.color.title)


class Size(models.Model):
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    size_system = models.CharField(max_length=20, default='')
    quantity = models.IntegerField(default=0)

    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="+")
    modified_by = models.ForeignKey(UserProfile, null=True, editable=False, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="+")

    def __str__(self):
        return self.name
