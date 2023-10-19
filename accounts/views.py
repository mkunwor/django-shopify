from django.shortcuts import render
from .forms import UserRegistrationForm,UserLoginForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .utils import send_account_activation_mail,generate_otp

class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("verify_otp_view")
 

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "An Activation Email Has Been Sent to You")
            response = self.form_valid(form)
            user = self.object
            send_account_activation_mail(request, user)
            jwt_payload = {"user_id": user.id}
            jwt_token = jwt.encode(jwt_payload, "SECRET_KEY", algorithm="HS256")

 

            # Set the token as a cookie
            response.set_cookie("jwt_token", jwt_token, httponly=True)

 

            messages.success(self.request, "An Activation Email Has Been Sent to You")
            return response
        else:
            return self.form_invalid(form)

def verify_otp(user, otp):
    print(user.id)
    try:
        otp_record = OtpVerificationModel.objects.get(user_id=user.id, otp=otp)
        print("otp record")
        print(otp_record)
        otp_record.delete()
        # Remove the OTP after successful verification
        return True
    except OtpVerificationModel.DoesNotExist:
        return False


def verify_otp_view(request):
    jwt_token = request.COOKIES.get("jwt_token")

 

    if jwt_token:
        try:
            # Verify the token
            jwt_payload = jwt.decode(jwt_token, "SECRET_KEY", algorithms=["HS256"])
            user_id = jwt_payload.get("user_id")
            user = User.objects.get(id=user_id)

 

            if request.method == "POST":
                form = OTPVerificationForm(request.POST)
                if form.is_valid():
                    submitted_otp = form.cleaned_data["otp"]
                    print(submitted_otp)
                    print("55", user.id)

 

                    if verify_otp(user, submitted_otp):
                        current_user = User.objects.get(id=user.id)
                        print(current_user)
                        current_user.email_verification_status = True
                        current_user.save()

 

                        return render(request, "accounts/login.html")
                    else:
                        # Invalid OTP, show an error message to the user
                        error_message = "Invalid OTP"
                else:
                    error_message = "Invalid form submission"
            else:
                form = OTPVerificationForm()
                error_message = None

 

            return render(
                request,
                "accounts/otp_form.html",
                {"form": form, "error_message": error_message},
            )
        except jwt.ExpiredSignatureError:
            # Handle expired token
            pass
        except jwt.DecodeError:
            # Handle invalid token
            pass
        except User.DoesNotExist:
            # Handle if user with that ID does not exist
            pass
    else:
        # No token found, handle the case as needed
        pass

class LoginView(FormView):
    form_class = UserLoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("dashboard:customer_dashboard")

 

    def dispatch(self, request, *args, **kwargs):
        pass