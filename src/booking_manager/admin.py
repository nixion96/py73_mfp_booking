from django.contrib import admin
from .models import Bookings


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'service', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('client', 'service')
    ordering = ('-date', '-time')
    list_editable = ('status',)
    list_per_page = 20
