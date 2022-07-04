from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.reports), name='reports'),
    path('export/all/', login_required(views.export_all), name='export_all'),
]