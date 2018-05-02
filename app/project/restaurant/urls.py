from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from project.restaurant.views.restaurant import RestaurantGetPostDeleteView, RestaurantGetListView, \
    RestaurantPostNewView, RestaurantCategoryView, RestaurantCreatorView
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
    # ME ##########################
    path(
        route='me/',
        view=GetUpdateUserProfileView.as_view(),
        name='get_update_user_profile',
    ),
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
    path(
        route='restaurants/category/<int:pk>/',
        view=RestaurantCategoryView.as_view(),
        name='restaurant_category'
    ),
    path(
        route='restaurants/user/<int:pk>/',
        view=RestaurantCreatorView.as_view(),
        name='restaurant_creator'
    ),
    path(
        route='restaurants/<int:pk>/',
        view=RestaurantGetPostDeleteView.as_view(),
        name='restaurant_editor'
    ),
    # path(),
    # path(),
    # path(),
]
