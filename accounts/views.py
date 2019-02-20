from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.forms import AccountsRegisterForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form = AccountsRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Your account has been successfull created! Please Login')
            return redirect('login')
        else:
            messages.error(request,'Testing error message')
    else:
        form = AccountsRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def logout(request):
    return render(request, 'accounts/logout.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

