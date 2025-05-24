# catalog/models.py (пример)
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True) # image_path
    slug = models.SlugField(unique=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='providers/profile/', blank=True, null=True) # profile_image_path
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255)
    categories = models.ManyToManyField(Category, related_name='providers') # Provider_Categories

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProviderImage(models.Model):
    provider = models.ForeignKey(Provider, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='providers/gallery/') # image_path
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f"Image for {self.provider.name}"