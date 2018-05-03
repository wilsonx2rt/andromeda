from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from project.restaurant.views.comments import NewCommentView, AllCommentsByUserView, \
    GetEditDeleteCommentView, LikeUnlikeCommentView
from project.restaurant.views.restaurant import RestaurantGetPostDeleteView, RestaurantGetListView, \
    RestaurantPostNewView, RestaurantCategoryView, RestaurantCreatorView
from project.restaurant.views.registration import RegistrationView, RegistrationValidationView
from project.restaurant.views.me import GetUpdateUserProfileView
from project.restaurant.views.restaurant_reviews import RestaurantsReviewOneRestaurantView, RestaurantUserReviews, \
    ReviewsAllPurpose
from project.restaurant.views.users import UserListView, GetUserById

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
    # USERS ###########################
    path(
        route='users/list/',
        view=UserListView.as_view(),
        name='get_user_list',
    ),
    path(
        route='users/<int:user_id>/',
        view=GetUserById.as_view(),
        name='get_user_by_id',
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
    ## REVIEWS ##################################
    path(
        route='reviews/restaurant/<int:pk>/',
        view=RestaurantsReviewOneRestaurantView.as_view(),
        name='restaurant_reviews'),

    path(
        route='reviews/restaurant/<int:pk>/',
        view=RestaurantsReviewOneRestaurantView.as_view(),
        name='restaurant_reviews'),

    path(route='reviews/user/<int:pk>/',
         view=RestaurantUserReviews.as_view(),
         name='user_reviews'),

    path(route='reviews/<int:pk>/',
         view=ReviewsAllPurpose.as_view(),
         name='reviews_allpurpose'),
    # COMMENTS #############################
    path(
        route='review/comment/new/<int:pk>/',
        view=NewCommentView.as_view(),
        name='new_comment',
    ),
    path(
        route='review/comment/<int:pk>/',
        view=GetEditDeleteCommentView.as_view(),
        name='delete_comment_by_id',
    ),
    path(
        route='review/comments/<int:user_id>/',
        view=AllCommentsByUserView.as_view(),
        name='get_all_comments_by_user_id',
    ),
    path(
        route='review/comment/like/<int:comment_id>/',
        view=LikeUnlikeCommentView.as_view(),
        name='like_unlike_comment_by_id',
    ),

    # path(),
    # path(),
    # path(),
]
