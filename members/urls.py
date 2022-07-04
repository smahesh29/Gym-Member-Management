from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/', login_required(views.add_member), name='add_member'),
    path('search/', login_required(views.search_member), name='search_member'),
    path('view/', login_required(views.view_member), name='view_member'),
    path('delete/<int:id>/', login_required(views.delete_member), name='delete_member'),
    path('update/<int:id>/', login_required(views.update_member), name='update_member'),
    path('', login_required(views.members), name='members'),
]