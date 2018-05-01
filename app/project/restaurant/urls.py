from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from project.restaurant.views.restaurant import RestaurantGetPostDeleteView, RestaurantGetListView, \
    RestaurantPostNewView
from project.restaurant.views.registration import RegistrationView, RegistrationValidationView

app_name = 'restaurant'

urlpatterns = [
    # AUTH #################################
    path(
        route='token/',
        view=TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        route='token/refresh/',
        view=TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        route='token/verify/',
        view=TokenVerifyView.as_view(),
        name='token_verify'
    ),
    # path(
    #     route='auth/password-reset/',
    #     view=PasswordResetCodeView.as_view(),cd
    #     name='password-reset-code'
    # ),
    # path(
    #     route='auth/password-reset/validate/',
    #     view=PasswordValidationView.as_view(),
    #     name='password-reset_verify'
    # ),
    # REGISTRATION ##########################
    path(
        route='registration/',
        view=RegistrationView().as_view(),
        name='registration',
    ),
    path(
        route='registration/validation/',
        view=RegistrationValidationView.as_view(),
        name='registration_validation'
    ),
    # RESTAURANT ###########################
    path(
        route='restaurants/',
        view=RestaurantGetListView.as_view(),
        name='all_restaurants'
         ),
    path(
        route='restaurants/new/',
        view=RestaurantPostNewView.as_view(),
        name='new_restaurant'
    ),
    # path(),
    # path(),
    # path(),
    # path(),
    # path(),
    # path(),
]
