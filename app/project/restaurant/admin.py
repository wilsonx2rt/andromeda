from django.contrib import admin

from project.restaurant.models import Restaurant, RestaurantReview, Comment
from project.user.userprofile import UserProfile

admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Comment)

