from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Building, RoomType, Room, BlockedDay
from .serializers import RoomSerializer, AvailableRoomSerializer

# Create your views here.

def index(request):
    return render(request,"index.html")



class AvailableRoomsAPIView(APIView):
    def get(self, request, format=None):
        check_in = request.query_params.get('check_in')
        check_out = request.query_params.get('check_out')
        building_name = request.query_params.get('building')
        try:
            building = Building.objects.get(name=building_name)
        except Building.DoesNotExist:
            return Response({'message': 'Building does not exist'}, status=status.HTTP_404_NOT_FOUND)
        rooms = Room.objects.filter(room_type__building=building).exclude(blockedday__day__range=(check_in, check_out)).distinct()
        if rooms:
            available_rooms = rooms.order_by('price')
            serializer = AvailableRoomSerializer(available_rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No rooms available'}, status=status.HTTP_404_NOT_FOUND)
 