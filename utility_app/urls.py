from django.urls import path
from . import views

app_name = 'utility_app'
urlpatterns = [
    path('', views.LandingPageView.as_view(), name="landing-page"),
    path('add-donation/', views.AddDonationView.as_view(), name="add-donation"),
]
