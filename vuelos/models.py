from django.db import models

# Create your models hfrom django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=255)
    flight_type = models.CharField(max_length=20, choices=[
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
