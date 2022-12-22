from django.db import models

# Create your models here.
class Gear(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  active = models.BooleanField(default=True)


  def __str__(self):
    return self.name
