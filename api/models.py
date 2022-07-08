from django.db import models

# Create your models here.


class Track(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    albumart = models.ImageField(
        upload_to="media/%Y/%m/%d", max_length=255, default="")
    mediafile = models.FileField(
        upload_to="media/", max_length=255, default="")

    class Meta:
        unique_together = ['order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
