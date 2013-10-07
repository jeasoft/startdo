from django.contrib.auth.models import User
from django.template import defaultfilters
from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name         = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=200, unique=True)
    description  = models.TextField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Company(models.Model):

    class Meta:
        verbose_name_plural = "companies"

    name         = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=200, unique=True)
    display_img  = models.ImageField(upload_to="company/images", blank=True, null=True)
    category     = models.ForeignKey(Category)
    website      = models.URLField(blank=True, null=True)
    twitter_url  = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    created_by   = models.ForeignKey(User)
    created_at   = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Company, self).save(*args, **kwargs)


