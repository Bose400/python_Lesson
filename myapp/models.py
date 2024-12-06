
from django.db import models

class Toy(models.Model):
    name = models.CharField(max_length=100)  # Toy name
    toy_type = models.CharField(max_length=50)  # Type of toy
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Price
    stock = models.IntegerField()  # How many toys available

    def __str__(self):
        return self.name