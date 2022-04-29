from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):

    def get(self, request):
        return render(request, "users_app/login.html")

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']
        print(f"username -> {username} password -> {password}")
        user = User.objects.filter(username=username, password=password)
        # user = authenticate(username=username, password=password)
        if user:
            login(request, user[0])
            return redirect("utility_app:landing-page")
        return redirect("users_app:register")


class RegisterView(View):

    def get(self, request):
        return render(request, "users_app/register.html")

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 and password1 != password2:
            return render(request, "users_app/register.html", {'msg': "hasła nie są takie same"})
        if name and surname and email and password1:
            new_user = User.objects.create(
                first_name=name,
                last_name=surname,
                username=email,
                password=password1,
                email=email,
            )
            return redirect('users_app:login')
        return render(request, "users_app/register.html", {'msg': "Wypełnij wszystkie pola"})


class LogoutView(View, LoginRequiredMixin):

    def get(self, request):
        logout(request)
        return redirect('utility_app:landing-page')

