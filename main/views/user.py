from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Passwords Do Not Match! Try Again')
            return redirect('Register')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Already Exists!')
            return redirect('Register')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email Address Already Exists!')
            return redirect('Register')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, '✅ Regristration Successful!')
        return redirect('Register')

    return render(request, 'Register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Does Not Exist!')
            return redirect('Login')

        if user is None:
            messages.error(request, '⚠️ Username or Password Is Incorrect!!')
            return redirect('Login')

        if user is not None:
            login(request, user)
            return redirect(reverse('Recommendations'))

    return render(request, 'Login.html')


@login_required(login_url='Login')
def Logout(request):
    logout(request)
    messages.success(request, '✅ Successfully Logged Out!')
    return redirect(reverse('Login'))
