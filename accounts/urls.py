from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', login_required(views.homepage_after_login), name="homepage_after_login"),
    path('wallpaper/', login_required(views.set_wallpaper), name="set_wallpaper"),
    path('change_password/', login_required(views.change_password), name='change_password'),
]+ static(settings.WALLPAPER_FILES, document_root=settings.WALLPAPER_URL)