from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):   
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    subdistrict = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    
class Finance(models.Model):
    bank = models.CharField(max_length=100)
    account_number = models.CharField(
        max_length=20, 
        unique=True,
        validators=[RegexValidator(r'^\d{1,20}$')]
    )
    
class Users(models.Model):
    name_user = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    ktp_number = models.CharField(
        max_length=16, unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d+$',  # Hanya angka
                message='KTP number must be numeric.',
                code='invalid_ktp_number'
            )
        ]
    ) 
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d+$',  # Hanya angka
                message='Phone number must be numeric.',
                code='invalid_phone_number'
            )
        ]
    )
    password = models.CharField(max_length=128)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)
    Finance = models.ForeignKey(Finance, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_user
    
    
class TypeProject(models.Model):
    type_project = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_project

class UsersProyect(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.users.name_user

class ProjectData(models.Model):
    name_project = models.CharField(max_length=50)
    type_project = models.ForeignKey(TypeProject, on_delete=models.CASCADE)
    location_project = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    Users = models.ForeignKey(UsersProyect, on_delete=models.CASCADE)  # id petani
   
    def __str__(self):
        return self.name_project

    