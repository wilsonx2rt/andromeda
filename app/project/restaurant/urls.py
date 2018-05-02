from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from project.restaurant.views.registration import RegistrationView, RegistrationValidationView
from project.restaurant.views.me import GetUpdateUserProfileView

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
        name='registration_validation'),

    # ME ##########################
    path(
        route='me/',
        view=GetUpdateUserProfileView.as_view(),
        name='get_update_user_profile',
    ),
    # path(
    #     route='registration/validation/',
    #     view=RegistrationValidationView.as_view(),
    #     name='registration_validation'),
]
