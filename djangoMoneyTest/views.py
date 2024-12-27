from django.shortcuts import render
from .forms import ReservationForm



def index(request):
	form = ReservationForm()
	return render(request, 'djangoMoneyTest/index.html', {'form': form})
