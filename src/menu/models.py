from django.db import models
from django.utils.text import slugify


class MenuModel(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(MenuModel, self).save(*args, **kwargs)
