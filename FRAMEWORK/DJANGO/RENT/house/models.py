from django.db import models
import uuid
# Create your models here.

class Landlord(models.Model):
    landlord_name = models.CharField(max_length=200, null=True, blank=True)
    landlord_phone = models.CharField(max_length=200, null=True, blank=True)
    landlord_email = models.EmailField(max_length=200, null=True, blank=True)
    landlord_idcard = models.CharField(max_length=200, null=True , blank=True)
    landlord_address = models.CharField(max_length=200, null=True, blank=True)
    landlord_password = models.CharField(max_length=200, null=True, blank=True)
    landlord_username = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    landlord_id = models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
        )

    def __str__(self):
        return self.landlord_username


class Tenant(models.Model):
    tenant_name = models.CharField(max_length=200, null=True, blank=True)
    tenant_phone = models.CharField(max_length=200, null=True, blank=True)
    tenant_email = models.EmailField(max_length=200, null=True, blank=True)
    tenant_idcard = models.CharField(max_length=14, null=True, blank=True)
    tenant_password = models.CharField(max_length=200, null=True, blank=True)
    tenant_username = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tenant_id = models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
        )

def __str__(self):
        return self.tenant_username


class Cite(models.Model):
    cite_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    council = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    number_slot = models.IntegerField(null=True, blank=True)
    town = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    cite_type = models.CharField(max_length=10, null=True, blank=True)
    cite_image = models.ImageField(null=True, blank=True, upload_to="home", default="home/BSD_GreatJones_287.jpg")
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    apartment= models.OneToOneField('Apartment', on_delete=models.CASCADE, null=True, blank=True)
    studio = models.OneToOneField('Studio', on_delete=models.CASCADE, null=True, blank=True)
    room= models.OneToOneField('Room', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    cite_id = models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
        )
        
    def __str__(self):
        return str(self.cite_id)

class Apartment(models.Model):
    number_of_room = models.IntegerField(null=True, blank=True)
    wardrobe = models.BooleanField(null=True, blank=True) 
    air_condition = models.BooleanField(null=True, blank=True)
    dimension = models.CharField(max_length=6, null=True, blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    light = models.BooleanField(null=True, blank=True)
    water = models.BooleanField(null=True, blank=True)
    number_of_bathroom = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    apartment_id = models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
        )
    
    def __str__(self):
        return str(self.apartment_id)

class Studio(models.Model):
    wardrobe = models.BooleanField(null=True, blank=True)
    air_condition = models.BooleanField(null=True, blank=True)
    dimension = models.CharField(max_length=6, null=True, blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    light = models.BooleanField(null=True, blank=True)
    water = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    studio_id = models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
        )
    
    def __str__(self):
        return str(self.studio_id)

class Room(models.Model):
    wardrobe = models.BooleanField(null=True, blank=True)
    kitchen = models.BooleanField(null=True, blank=True)
    dimension = models.CharField(max_length=6, null=True, blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    light = models.BooleanField(null=True, blank=True)
    water = models.BooleanField(null=True, blank=True)
    toilet = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    room_id = models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
        )
    
    def __str__(self):
        return str(self.room_id)