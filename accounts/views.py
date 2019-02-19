from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method=='POST':
        message.success(f'Your account has been successfully created! Please login')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')
def logout(request):
    return render(request, 'accounts/logout.html')
def register(request):
    return render(request, 'accounts/register.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

