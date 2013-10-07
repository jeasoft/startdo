from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

# I just could have created choices for UserProfile class
# but I don't know how many categories of users this could have
class Industry(models.Model):
    class Meta:
        verbose_name_plural = "industries"

    name =  models.CharField(max_length=100)
    slug =  models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Industry, self).save(*args, **kwargs)

#Patience :P
class UserProfile(models.Model):
    user        = models.OneToOneField(User)
    avatar      = models.ImageField(upload_to="users/imgs/avatar",blank=True ,null=True)
    industry    = models.ForeignKey(Industry) 
    description = models.TextField()

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return ("{} {}".format(self.user.first_name, self.user.last_name))
        else:
            return self.user.username



class Skill(models.Model):
    name =  models.CharField(max_length=100)
    slug =  models.SlugField(max_length=100, unique=True)
    user =  models.ForeignKey(User)

    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Skill, self).save(*args, **kwargs)