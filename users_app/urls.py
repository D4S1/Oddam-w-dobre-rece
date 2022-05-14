from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("donations/", views.DonationsView.as_view(), name="donations"),
    path("archive-donation/<int:pk>", views.ArchiveDonationView.as_view(), name="archive-donation"),
    path("edit-profile/", views.EditProfileView.as_view(), name="edit-profile"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]
