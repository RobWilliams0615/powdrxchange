from django.db import models


class GearPlatForm(models.Model):
  store_name = models.CharField(max_length=100)
  store_address = models.CharField(max_length=100)
  store_city = models.CharField(max_length=100)
  store_state = models.CharField(max_length=100)
  store_zip = models.CharField(max_length=100)
  store_country = models.CharField(max_length=100)
  store_phone = models.CharField(max_length=100)
  store_website = models.URLField(max_length=100)
  store_description = models.CharField(max_length=500)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.store_name

class Gear(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.name
