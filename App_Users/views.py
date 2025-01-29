from django.shortcuts import render, redirect

# from django.contrib.auth.decorators import login_required
from App_Main.models import MyPersonal
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserProfileUpdateForm, CommentForm
from .models import Comments, Users
from django.http import JsonResponse


def logout_view(request):
    logout(request)

    # Redirect to a success page.



from django.http import JsonResponse

def ContactView(request):
    person = MyPersonal.objects.first()
    if request.method == "POST":
        full_name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        body = request.POST.get("message", "").strip()

        owner = None
        if request.user.is_authenticated:
            owner = request.user
            full_name = request.user.get_full_name() or "Anonymous"
            email = request.user.email

        if subject and body:
            Comments.objects.create(
                owner=owner,
                full_name=full_name,
                email=email,
                subject=subject,
                body=body,
            )
            return JsonResponse({"message": "Message sent successfully!"})  # Success javobi

        return JsonResponse({"message": "Subject and message are required!"}, status=400)  # Xato javobi

    return render(request, "App_Users/contact.html", {"person": person})


class UserRegistration(CreateView):
    template_name = "App_Users/registration.html"
    model = Users
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    extra_context = {
        "footer_fixed": True,
    }

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET" and request.user.is_authenticated:
            return redirect("home")

        return super().dispatch(request, *args, **kwargs)


@login_required
def user_profile_view(request):
    person = MyPersonal.objects.first()

    user = request.user
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")  # Profil sahifasiga qaytarish
    else:
        form = UserProfileUpdateForm(instance=user)
    return render(
        request,
        "App_Users/user_profile.html",
        {"form": form, "fullname": user.fullname,'person':person},
    )
