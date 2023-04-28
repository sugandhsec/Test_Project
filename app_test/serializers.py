from rest_framework import serializers
from .models import Building, RoomType, Room, BlockedDay


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class AvailableRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'price', 'room_type']
