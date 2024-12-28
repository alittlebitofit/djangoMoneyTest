from django.db import models

# Create your models here.



from djmoney.models.fields import MoneyField

class Reservation(models.Model):
	tip = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')




class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Store as "+1234567890"
    country = models.CharField(max_length=100)  # Automatically derived from country code
