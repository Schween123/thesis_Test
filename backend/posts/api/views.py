from rest_framework import viewsets
from ..models import Owner, BoardingHouse, Room, Tenant, Guardian, Transaction, FaceImage
from .serializers import OwnerSerializer, BoardingHouseSerializer, RoomSerializer, TenantSerializer, GuardianSerializer, TransactionSerializer, FaceImageSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class BoardingHouseViewSet(viewsets.ModelViewSet):
    queryset = BoardingHouse.objects.all()
    serializer_class = BoardingHouseSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class GuardianViewSet(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class FaceImageViewSet(viewsets.ModelViewSet):
    queryset = FaceImage.objects.all()
    serializer_class = FaceImageSerializer
