from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime, timedelta
from .models import Building, RoomType, Room, BlockedDay
from .serializers import RoomSerializer 

class AvailableRoomsAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.building = Building.objects.create(name='Test Building')

        self.room_type = RoomType.objects.create(name='Test Room Type', type='Single', building=self.building)

        self.room1 = Room.objects.create(number=101, room_type=self.room_type, price=50.00)
        self.room2 = Room.objects.create(number=102, room_type=self.room_type, price=75.00)
        self.room3 = Room.objects.create(number=103, room_type=self.room_type, price=100.00)

        self.today = datetime.today()
        self.check_in = self.today + timedelta(days=1)
        self.check_out = self.today + timedelta(days=5)

        self.blocked_day1 = BlockedDay.objects.create(day=self.today, room=self.room1)
        self.blocked_day2 = BlockedDay.objects.create(day=self.check_in, room=self.room1)
        self.blocked_day3 = BlockedDay.objects.create(day=self.check_out, room=self.room2)

    def test_available_rooms_api_view(self):
        url = reverse('available_rooms_api_view')
        response = self.client.get(f'{url}?check_in={self.check_in.date()}&check_out={self.check_out.date()}&building={self.building.name}')
        rooms = Room.objects.filter(room_type__building__name=self.building.name).exclude(id__in=[self.blocked_day1.room.id, self.blocked_day2.room.id, self.blocked_day3.room.id]).order_by('price')
        serializer = RoomSerializer(rooms, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

