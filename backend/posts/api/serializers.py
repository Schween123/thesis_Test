from rest_framework import serializers
from ..models import Owner, BoardingHouse, Room, Tenant, Guardian, Transaction, FaceImage

class OwnerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'fingerprint', 'face_image', 'address', 'phone_number', 'vault_password']

class BoardingHouseSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Owner.objects.all())

    class Meta:
        model = BoardingHouse
        fields = ['id', 'bh_name', 'address', 'capacity', 'number_of_tenants', 'number_of_rooms', 'owner']

class RoomSerializer(serializers.ModelSerializer):
    boarding_house = serializers.SlugRelatedField(slug_field='bh_name', queryset=BoardingHouse.objects.all())

    class Meta:
        model = Room
        fields = ['boarding_house', 'room_number', 'capacity', 'available_beds']

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'address', 'relationship']

class TenantSerializer(serializers.ModelSerializer):
    guardian = serializers.PrimaryKeyRelatedField(queryset=Guardian.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Tenant
        fields = ['id', 'first_name', 'last_name', 'image_id', 'gender', 'age', 'course_profession', 'school_company', 'address', 'phone_number', 'monthly_due', 'monthly_due_date', 'guardian', 'room', 'initial_payment']

class TransactionSerializer(serializers.ModelSerializer):
    tenant = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'transaction_date', 'transaction_time', 'mode_of_payment', 'amount_paid', 'month_status', 'tenant']

class FaceImageSerializer(serializers.ModelSerializer):
    tenant = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())

    class Meta:
        model = FaceImage
        fields = ['image_id', 'tenant', 'face_image', 'time_stamp']
