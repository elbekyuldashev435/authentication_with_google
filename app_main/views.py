from django.shortcuts import render, redirect

# Create your views here.


def get_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'app_main/home.html')