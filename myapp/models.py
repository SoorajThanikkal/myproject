from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    # latitude = models.FloatField()
    # longitude = models.FloatField()

    def __str__(self):
        return self.name
class upload(models.Model):
    image = models.ImageField(upload_to='obj/')

