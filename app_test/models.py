from django.db import models

# Create your models here.
from django.db import models
ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
    ]
class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()}) in {self.building.name}"

class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"Room {self.number} ({self.room_type.name} in {self.room_type.building.name})"


class BlockedDay(models.Model):
    day = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"Blocked day {self.day} for Room {self.room.number} ({self.room.room_type.name} in {self.room.room_type.building.name})"
