from django.shortcuts import render, redirect
from soteq.other_function import is_connected
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def signup(request):
    connected = is_connected(request)
    if request.method == 'POST':
        username=request.POST.get('username')
        print(username)
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if (password == confirm_password):
                User.objects.create_user(username, 'lennon@thebeatles.com', password)
                user = authenticate(username=username, password=password)
                login(request,user)
            return redirect('produits')
        # user.save()
        return redirect('index')
    context = {
        "connected": connected,
        # "form": form,
    }
    return render(request, 'signup.html', context)