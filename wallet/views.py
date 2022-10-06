from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from app_user.models import AppUser
import requests

# Create your views here.

@login_required(login_url='/app/sign-in/')
def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/loop-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s" % (app_user.wallet_address)).json()
		data = [resp["data"][1]]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/index.html", context )




		
@login_required(login_url='/app/sign-in/')
def SendView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-loop/", data={"sender": sender,"sender_key": sender_key, "receiver": receiver, "amount": amount, "token_address": token_address})
			SendB(sender, sender_key, receiver, amount, token)
			messages.warning(request, "Success: %s" % (txn_hash))
			return HttpResponseRedirect(reverse("wallet:index"))
		except:
			messages.warning(request, "Not successfully")
			return HttpResponseRedirect(reverse("wallet:index"))
				
				
		
	else:
		
		
		
		context = {"app_user": app_user}
		return render(request, "wallet/withdraw.html", context)
		
@login_required(login_url='/app/sign-in/')
def SendTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if token_address == "0x3936D20a39eD4b0d44EaBfC91757B182f14A38d5":
			token = "loop"
		
		elif token_address == "0x3030BbB60574f7DFC989f3ab6cf4fDd1E8A519A9":
			token = "sphynx-labs"
		
		
		
		
			#name = "Brise"
		else:
			#pass
			try:
				resp = requests.post("https://api.iotexchartapp.com/send-loop/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
				txn_hash = resp["txn_hash"]
				messages.success(request, "Success: %s" % (txn_hash))
				return HttpResponseRedirect(reverse("wallet:index"))
			except Exception as e:
				messages.warning(request, "Not successfull out of Gas")
				#print e
				return HttpResponseRedirect(reverse("wallet:index"))
		
	else:
		resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x3936D20a39eD4b0d44EaBfC91757B182f14A38d5":
			token = "loop"
			token_name = "LoopNetwork"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0x3030BbB60574f7DFC989f3ab6cf4fDd1E8A519A9":
			token = "sphynx-labs"
			token_name = "SPHYNX"
			brise_balance = data[5]["balance"]
			token_logo = data[5]["logo"]
		
		
		context = {"app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_token.html", context)


		
		


		
#def error_404(request, exception):
	#return render(request,'app_user/404.html')

#def error_500(request):
	#return render(request,'app_user/500.html')


