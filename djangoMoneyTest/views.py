from django.shortcuts import render
from .forms import ReservationForm
from djmoney.settings import CURRENCY_CHOICES


def index(request):
	form = ReservationForm()
	print(CURRENCY_CHOICES)
	return render(request, 'djangoMoneyTest/index.html', {'form': form})
