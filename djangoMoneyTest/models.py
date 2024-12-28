from django.db import models

# Create your models here.



from djmoney.models.fields import MoneyField

class Reservation(models.Model):
	tip = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')





class Employee(models.Model):
    first_name = models.CharField(max_length=50, default="omg")
    profile_picture = models.ImageField(upload_to='employee_images/')

    def __str__(self):
        return f"{self.first_name}"
