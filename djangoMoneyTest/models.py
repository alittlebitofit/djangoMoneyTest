from django.db import models

# Create your models here.



from djmoney.models.fields import MoneyField

class Reservation(models.Model):
	tip = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
