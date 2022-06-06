from django.db import models
class Phones(models.Model):
    City = models.CharField(max_length=255)
    Date = models.CharField(max_length=255)
    Brand = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Storage = models.IntegerField()
    Stat = models.CharField(max_length=255)
    Price = models.IntegerField()

    # def __str__(self):
    #     return self.name
