from django.shortcuts import render
from django.views import View
from django.db.models import Sum

from . import models


class LandingPageView(View):

    def get(self, request):
        bags = models.Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        institutions = models.Institution.objects.all().count()
        return render(request, 'utility_app/index.html', {
            'bags': bags,
            'institutions': institutions,
        })


class AddDonationView(View):

    def get(self, request):
        return render(request, 'utility_app/form.html')

    def post(self, request):
        pass
