from django.shortcuts import render
from django.views import View


class LoginView(View):

    def get(self, request):
        return render(request, "users_app/login.html")

    def post(self, request):
        pass


class RegisterView(View):

    def get(self, request):
        return render(request, "users_app/register.html")

    def post(self, request):
        pass
