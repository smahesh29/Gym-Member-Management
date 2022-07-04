from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('delete/<int:id>/', login_required(views.notification_delete), name='notification_delete'),
    path('', login_required(views.notifications), name='notifications'),
]