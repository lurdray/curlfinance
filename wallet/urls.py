from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [

	path("", views.IndexView, name="wallet"),
	path("withdraw/", views.SendView, name="withdraw"),
	path("send-token/<str:token_address>/", views.SendTokenView, name="send_token"),
	
]