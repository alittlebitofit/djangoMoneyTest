import os

from django.conf import settings
from django.contrib.auth.decorators import login_not_required
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect

from .forms import ReservationForm
from .forms import EmployeeForm
from .models import Employee



@login_not_required
def index(request):
	form = ReservationForm()
	return render(request, 'djangoMoneyTest/index.html', {'form': form})




def employee_list(request):
	employees = Employee.objects.all()
	return render(request, 'djangoMoneyTest/employee_list.html', {'employees': employees})




def upload_employee(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dmt:employee-list')  # Redirect to a list view or success page
	else:
		form = EmployeeForm()
	return render(request, 'djangoMoneyTest/upload_employee.html', {'form': form})




def protected_media(request, path):
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(media_path):
        return FileResponse(open(media_path, 'rb'))
    raise Http404("File not found")
