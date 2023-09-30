from django.contrib import admin
from .models import Movie, Reservation, Guest, Post
# Register your models here.
admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Guest)
admin.site.register(Post)
