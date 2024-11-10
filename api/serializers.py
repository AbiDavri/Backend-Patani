from rest_framework import serializers
from .models import Users, Address, Finance, ProjectData, TypeProject

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'province', 'city', 'district', 'subdistrict', 'postal_code']

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = ['id', 'bank', 'account_number']

class UserSerializer(serializers.ModelSerializer):
    Address = AddressSerializer()  # Menggunakan AddressSerializer
    Finance = FinanceSerializer()  # Menggunakan FinanceSerializer

    class Meta:
        model = Users
        fields = ['id', 'name_user', 'email', 'ktp_number', 'phone_number', 'password', 'Address', 'Finance']

    def create(self, validated_data):
        address_data = validated_data.pop('Address')
        finance_data = validated_data.pop('Finance')
        
        # Membuat instance Address
        address = Address.objects.create(**address_data)
        
        # Membuat instance Finance
        finance = Finance.objects.create(**finance_data)
        
        # Membuat instance Users
        user = Users.objects.create(Address=address, Finance=finance, **validated_data)
        
        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('Address', None)
        finance_data = validated_data.pop('Finance', None)

        # Update Users instance
        instance.name_user = validated_data.get('name_user', instance.name_user)
        instance.email = validated_data.get('email', instance.email)
        instance.ktp_number = validated_data.get('ktp_number', instance.ktp_number)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        # Update Address instance
        if address_data:
            for attr, value in address_data.items():
                setattr(instance.Address, attr, value)
            instance.Address.save()

        # Update Finance instance
        if finance_data:
            for attr, value in finance_data.items():
                setattr(instance.Finance, attr, value)
            instance.Finance.save()

        return instance

class TypeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProject
        fields = ['id', 'type_project'] 
        
class UsersProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name_user']

class ProjectDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectData
        fields = [
            'id', 
            'name_project', 
            'type_project', 
            'location_project', 
            'start_date', 
            'end_date', 
            'Users',
        ]