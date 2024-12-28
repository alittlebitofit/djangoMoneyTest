from django import forms
from .models import Reservation, Employee





class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ['tip']




class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'profile_picture']
