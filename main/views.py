from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required




from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm

from datetime import datetime
from requests import Request, Session
import json
import time
from datetime import datetime, timedelta





def ConnectMetamaskManualView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_manual.html", context)
		
def ConnectMetamaskView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask.html", context)




def PortfolioView(request):
	if request.method == "POST":
		pass

	else:
		try:
			total = 0
			wallet = request.session["wallet"]
			
			resp = requests.get("https://api.iotexchartapp.com/get-balance/%s/" % str(wallet)).json()
			data = resp["data"]
			
			for item in data:
				total += float(item['total_price'])

			#return HttpResponse(data)
			context = {"data": data, "total": total, "wallet": wallet}
			return render(request, "main/portfolio.html", context)
			
		except:
			return HttpResponseRedirect(reverse("main:your_portfolio"))



def NoneView(request):
	if request.method == "POST":
		pass

	else:

		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		doken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		
		context = {"cronos":cronos, "data":data,}
		return render(request, "main/none.html", context)

def GetUrlViaAddress(address):
		
	if address == "0xf9a2d40589271be17612a3f57a9028a568f56e3d":
		url = "doken"
	elif address == "0xce186ad6430e2fe494a22c9edbd4c68794a28b35":
		url = "loop"
	
	

	else:
		url = "loop"


	return url

def GetUrlViaName(name):

	if name == "Doken Super Chain (DSC)":
		url = "doken"
	elif name == "LoopNetwork (LOOP)":
		url = "loop"
	
	
    
	    
	else:
		url = "loop"

	return url


def IndexView(request):
	if request.method == "POST":
		address_db = [
		"0xf9a2d40589271be17612a3f57a9028a568f56e3d", "0xce186ad6430e2fe494a22c9edbd4c68794a28b35",
		]

		name_db = ["Doken Super Chain (DSC)", "LoopNetwork (LOOP)"]

		status = False
		result = None
		url = "none"

		query = request.POST.get("query")

		if query[0]+query[1] == "0x":
			for item in address_db:
				if query == item:
					result = item
					url = GetUrlViaAddress(result)


		for item in name_db:
			if query == item or query in item:
				result = item

				url = GetUrlViaName(result)


		return HttpResponseRedirect(reverse("main:%s" % (url)))
		


	else:
		#data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		doken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		loop = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=loopnetwork&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		emvos = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=evmos&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		sweat = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sweatcoin&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cosmos = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cosmos&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		bnb = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=binancecoin&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cronos = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		trending = requests.get("https://api.coingecko.com/api/v3/search/trending")
		market = requests.get("https://api.coingecko.com/api/v3/global")
		trend = trending.json()
		coins = trend["coins"][:4]
		mcap = market.json()
		m_data = mcap["data"]

		
		



		
		context = {"doken":doken,"loop":loop, "emvos":emvos, "sweat":sweat, "cosmos":cosmos, "bnb":bnb, "cronos":cronos, "coins":coins, "m_data":m_data}
		return render(request, "main/index.html", context )

        
        
def DokenView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=doken&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xf9a2d40589271be17612a3f57a9028a568f56e3d")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["doken"]["usd"])
        market_cap = int(response["doken"]["usd_market_cap"])
        hr_vol = str(response["doken"]["usd_24h_vol"])
        hr_chg = str(response["doken"]["usd_24h_change"])
        last_updated = str(response["doken"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/doken.html", context)


def LoopView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=loopnetwork&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=loopnetwork&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xce186ad6430e2fe494a22c9edbd4c68794a28b35")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["loopnetwork"]["usd"])
        market_cap = int(response["loopnetwork"]["usd_market_cap"])
        hr_vol = str(response["loopnetwork"]["usd_24h_vol"])
        hr_chg = str(response["loopnetwork"]["usd_24h_change"])
        last_updated = str(response["loopnetwork"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/loop.html", context)
        

        
        
