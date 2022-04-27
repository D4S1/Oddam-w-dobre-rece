from django.shortcuts import render
from django.views import View


class LandingPageView(View):

    def get(self, request):
        return render(request, 'utility_app/index.html')


class AddDonationView(View):

    def get(self, request):
        return render(request, 'utility_app/form.html')

    def post(self, request):
        pass
