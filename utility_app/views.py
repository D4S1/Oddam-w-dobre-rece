from django.shortcuts import render
from django.views import View
from django.db.models import Sum

from . import models


def get_institution_ifo(type):
    return [
            (institution, ", ".join([cat['name'] for cat in institution.categories.all().values('name')]))
            for institution in models.Institution.objects.filter(type=type)
        ]


class LandingPageView(View):

    def get(self, request):
        # dynamic counting
        bags = models.Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        institutions = models.Institution.objects.all().count()

        # help section
        foundations = get_institution_ifo('Fundacja')
        organisations = get_institution_ifo('Organizacja')
        locals = get_institution_ifo("Zbiórka lokalna")

        # print(models.Institution.objects.get(pk=1).categories.all().values('name'))
        return render(request, 'utility_app/index.html', {
            'bags': bags,
            'institutions_counter': institutions,
            'foundations': foundations,
            'organisations': organisations,
            'locals': locals,
        })


class AddDonationView(View):

    def get(self, request):
        return render(request, 'utility_app/form.html')

    def post(self, request):
        pass
