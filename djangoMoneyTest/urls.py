from django.urls import path
from . import views

app_name='dmt'

urlpatterns = [
	path('', views.index, name='index'),
	path('upload-image/', views.upload_employee, name='upload-image'),
	path('employee-list/', views.employee_list, name='employee-list'),
]


urlpatterns += [
	path('media/<path:path>', views.protected_media, name='protected-media'),
]