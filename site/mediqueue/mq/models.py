from django.db import models

class Doctors(models.Model):
    title = models.CharField(max_length=45)
    specialnost = models.TextField(max_length=45)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
