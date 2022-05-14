from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

from datetime import datetime
from ast import literal_eval


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


class AddDonationView(LoginRequiredMixin, View):

    def get(self, request):
        categories = models.Category.objects.all()
        institutions = models.Institution.objects.all()
        organisations = [(organisation, ','.join(str(category.pk) for category in organisation.categories.all()))
                         for organisation in institutions]
        return render(request, 'utility_app/form.html', {
            'categories': categories,
            'organisations': organisations,
        })

    def post(self, request):
        bags = request.POST['bags']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['postcode']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        time = request.POST['time']
        categories = [int(ele) for ele in request.POST.getlist('category')]
        organisation = request.POST['organisation']
        notice = request.POST['more_info']


        if bags and address and city and zip_code and phone and date and time and categories and organisation:
            new_donation = models.Donation.objects.create(
                quantity=bags,
                institution_id=organisation,
                address=address,
                phone_number=phone,
                city=city,
                zip_code=zip_code,
                pick_up_date=datetime.strptime(date, "%Y-%m-%d").date(),
                pick_up_time=datetime.strptime(time, '%H:%M').time(),
                pick_up_comment=notice,
                user=request.user,
            )
            print(f"new donation -> {new_donation}")
            new_donation.categories.set(categories)

        return redirect("utility_app:donation-confirmation")


class ConfirmationView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "utility_app/form-confirmation.html")
