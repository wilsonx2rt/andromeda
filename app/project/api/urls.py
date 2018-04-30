from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'api'

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
    #     view=PasswordResetCodeView.as_view(),
    #     name='password-reset-code'
    # ),
    # path(
    #     route='auth/password-reset/validate/',
    #     view=PasswordValidationView.as_view(),
    #     name='password-reset_verify'
    # ),
]
