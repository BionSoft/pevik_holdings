from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    class ProjectType(models.TextChoices):
        DEVELOPMENT_PROJECT = 'Development Project'
        OFFPLAN_PROJECT = 'Off Plan Project'
        READY_PROJECT = 'Ready Project'

    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    project_type = models.CharField(max_length=50, choices=ProjectType.choices, default=ProjectType.DEVELOPMENT_PROJECT)
    price = models.IntegerField(blank=True)
    extimated_price = models.IntegerField(blank=True)
    featured = models.BooleanField(default=True, blank=True)
    units = models.IntegerField()
    project_logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    video_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    video_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)
    
    def __str__(self):
        return self.title
    