from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path("your-portfolio/manual/", views.ConnectMetamaskManualView, name="your_portfolio_manual"),
    path("your-portfolio/", views.ConnectMetamaskView, name="your_portfolio"),
    path("portfolio/", views.PortfolioView, name="portfolio"),
	path("", views.IndexView, name="index"),
	path("doken/", views.DokenView, name="doken"),
	path("loop/", views.LoopView, name="loop"),

]