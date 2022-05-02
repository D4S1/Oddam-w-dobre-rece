from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from utility_app import models


class LoginView(View):

    def get(self, request):
        return render(request, "users_app/login.html")

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
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
            new_user = User.objects.create_user(
                first_name=name,
                last_name=surname,
                username=email,
                password=password1,
                email=email,
            )
            return redirect('users_app:login')
        return render(request, "users_app/register.html", {'msg': "Wypełnij wszystkie pola"})


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect('utility_app:landing-page')


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        # user data
        name = request.user.first_name
        surname = request.user.last_name
        email = request.user.email
        # donations
        donations = models.Donation.objects.filter(user_id=request.user.pk).order_by('is_taken', '-pick_up_date')
        donations = [(donation, ', '.join([category.name for category in donation.categories.all()])) for donation in donations]
        return render(request, "users_app/user-profile.html", {
            'name': name,
            'surname': surname,
            'email': email,
            'donations': donations,
        })


class ArchiveDonationView(LoginRequiredMixin, View):

    def get(self, request, pk):
        donation = models.Donation.objects.get(pk=pk)
        donation.is_taken = True
        donation.save()
        return redirect('users_app:profile')


class EditProfileView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'users_app/edit-profile.html', {
            'name': request.user.first_name,
            'surname': request.user.last_name,
            'email': request.user.email,
        })

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        context = {
                'name': request.user.first_name,
                'surname': request.user.last_name,
                'email': request.user.email,
        }
        if not authenticate(username=request.user.username, password=password):
            context['msg'] = 'Nie poprawne hasło'
            return render(request, 'users_app/edit-profile.html', context)
        if name and surname and email:
            update = User.objects.get(pk=request.user.pk)
            update.first_name = name
            update.last_name = surname
            update.username, update.email = email, email
            update.save()
            return redirect("users_app:profile")

        context['msg'] = 'Wypełnij wszystkie pola'
        return render(request, 'users_app/edit-profile.html', context)


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'users_app/change-password.html')

    def post(self, request):
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        old_password = request.POST['old-password']
        user = authenticate(username=request.user.username, password=old_password)
        if not user:
            return render(request, 'users_app/change-password.html', {'msg': 'Nie poprawne stare hasło'})
        if password1 and password2 and password1 == password2:
            user.set_password(password1)
            user.save()
            return redirect('users_app:profile')
        return render(request, 'users_app/change-password.html', {'msg': 'Nie poprawne nowe hasło'})
