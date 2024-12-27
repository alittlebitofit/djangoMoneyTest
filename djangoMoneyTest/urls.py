from django.urls import path
from . import views

app_name='dmt'

urlpatterns = [
	path('', views.index, name='index'),
]
