from django.db import models
from django.urls import reverse

# Create your models here.

class Gear(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=20)
  weight = models.DecimalField(max_digits=3, decimal_places=2, default=0)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('gears_detail', kwargs={'pk': self.id})

class Hiker(models.Model):
  name = models.CharField(max_length=30)
  gears = models.ManyToManyField(Gear)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'hiker_id': self.id})

