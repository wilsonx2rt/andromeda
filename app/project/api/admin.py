from django.contrib import admin

from project.restaurant.models import User, Restaurant, RestaurantReview, Comment

from project.restaurant.models import Like

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Comment)
admin.site.register(Like)
