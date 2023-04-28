from django.contrib import admin
from app_test.models import *
# Register your models here.
admin.site.register(Building)
admin.site.register(RoomType)
# admin.site.register(Room)
# admin.site.register(BlockedDay)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_type', 'price')

@admin.register(BlockedDay)
class BlockedDayAdmin(admin.ModelAdmin):
    list_display = ('day', 'room')
