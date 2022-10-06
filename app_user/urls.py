from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [


	path("sign-in/", views.SignInView, name="sign_in"),
	path("sign-up/", views.SignUpView, name="sign_up"),
	path("maintain/", views.MaintainView, name="maintain"),
	path("sign-up/complete/", views.CompleteSignUpView, name="complete_sign_up"),
	path("sign-out/", views.SignOutView, name="sign_out"),
	
	path("forgot-password/", views.ForgotPasswordView, name="forgot_password"),
	path("set-new-password/", views.SetNewPView, name="set_new_p"),

	
	path("app-user-detail/<int:app_user_id>/", views.AppUserDetailView, name="app_user_detail"),
	
	path("<str:wallet_address>/", views.AppUserDetail2View, name="app_user_detail2"),

	path("temp/", views.TempView, name="temp"),
	path("change-password/", views.ChangePasswordView, name="change_password"),

]