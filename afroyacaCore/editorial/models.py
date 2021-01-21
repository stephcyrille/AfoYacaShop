from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from account.models import UserProfile


def articles_image_path(instance, filename):
    title = instance.title
    author = slugify(title)
    return "articles/%s/%s" % (title, author)


class Article(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=250, null=False, blank=False)
    guess = models.CharField(max_length=150, null=False, blank=False)
    photograph = models.CharField(max_length=150, null=False, blank=False)
    date = models.DateTimeField(null=True, blank=True)
    resume = models.TextField()
    content = models.TextField()
    facebookUrl = models.TextField(blank=True, null=True)
    twitterUrl = models.TextField(blank=True, null=True)
    whatsappUrl = models.TextField(blank=True, null=True)
    mailUrl = models.TextField(blank=True, null=True)
    coverImage = models.FileField(upload_to=articles_image_path, null=True, blank=True)
    articleImage = models.FileField(upload_to=articles_image_path, null=True, blank=True)
    cover = models.BooleanField(default=False)
    mainMenu = models.BooleanField(default=False)
    # Just for knowing if is the home cover magazine
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
        return '%s - %s' % (self.title, self.author)

    def get_cover_picture(self):
        """
        Get only one picture
        """
        return self.coverImage.url

    def get_article_picture(self):
        """
        Get only one picture
        """
        return self.articleImage.url