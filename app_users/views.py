from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
# Create your views here.


UserModel = get_user_model()


def login_user(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        return redirect("login")

    return render(request, "app_users/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


def signup_user(request):
    if request.POST:

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and password1 and password2 and password2 == password1:

            user = UserModel.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            user.set_password(password1)
            user.save()
            login(request, user)

            return redirect('home')
    return render(request, "app_users/register.html")