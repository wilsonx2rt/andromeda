from django.contrib import admin

from project.restaurant.models import Restaurant, RestaurantReview, Comment

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Comment)
