from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer
from .forms import ReservationForm
# from djmoney.settings import CURRENCY_CHOICES


def index(request):
	# file_path = 'currency.txt'
	# with open(file_path, 'w') as file:
	# 	for code, name in CURRENCY_CHOICES:
	# 		file.write(f"('{code}', '{name}')\n")
	# print(f'Currencies written to {file_path}')

	form = ReservationForm()
	return render(request, 'djangoMoneyTest/index.html', {'form': form})



def save_customer(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')  # Full phone number with country code
        country = request.POST.get('country')  # Country name

        # Save to database
        Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            country=country
        )

        return HttpResponse("Customer saved successfully!")
    return render(request, "djangoMoneyTest/customer_form.html")