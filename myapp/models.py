from django.db import models

# Create your models here.
class reservations(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    reservation_slot = models.SmallIntegerField(default=10)
    def __str__(self):
        return self.name
class menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    def __str__(self):
        return self.name