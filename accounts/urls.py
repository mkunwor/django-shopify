
from django.urls import path,include
from accounts import views


urlpatterns = [
     path('',views.UserRegistrationView.as_view(),name='register'),
    path("register/verify-otp/", views.verify_otp_view, name="verify_otp_view"),



]