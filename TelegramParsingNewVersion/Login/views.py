from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.
def page_login(request):
    return render(request=request, template_name='Login/Login.html')

def page_telegram(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    return render(request, 'Login/Telegram.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')