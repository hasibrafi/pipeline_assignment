from django.conf import settings
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .models import *
from .decorators import *

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

#login
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect!')

        context = {}
        return render(request, 'login.html', context)

#logout
def LogoutView(request):
    logout(request)
    return redirect('index')

#profile
#@unauthenticated_user
def Profile(request, id):
    user = User.objects.get(id=id)
    
    context = {'user': user}
    return render(request, 'profile.html', context)

#change-password
def ChangePasswordForm(request, id):

    context = {}
    return render(request, 'change-password.html', context)


#change-password
def ChangePassword(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']
        print(new_password, confirm_new_password)

        if new_password == confirm_new_password:
            user.set_password(new_password)
            user.save()
            #return render(request, 'password_confirmation.html', {'user':user})
            return redirect('index')
        else:
            messages.info(request, "Password didn't match!")

    context = {}
    return render(request, 'change-password.html', context)

#password_confirmation
def PasswordConfirmation(request, id):
    user = User.objects.get(id=id)

    context = {'user': user}
    return render(request, 'password_confirmation.html', context)