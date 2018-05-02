from django.contrib import admin

from project.api.models import User, Restaurant, RestaurantReview, Comment

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Comment)
