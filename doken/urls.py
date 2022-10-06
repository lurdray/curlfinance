from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("wallet/", include("wallet.urls")),
    path("app/", include("app_user.urls")),

]
