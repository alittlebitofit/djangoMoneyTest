from django.shortcuts import render, redirect
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


def google(request):
	return redirect('https://www.google.com/')