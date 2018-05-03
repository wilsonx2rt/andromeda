from django.contrib import admin

from project.restaurant.models import Restaurant, RestaurantReview, Comment, Category, Like

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Like)