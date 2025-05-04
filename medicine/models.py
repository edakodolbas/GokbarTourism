
from django.db import models
from django.contrib.auth.models import User


class SelectedCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.IntegerField()
    selection_count = models.IntegerField(default=0)  # Seçimin kaç kez yapıldığını takip eden alan
    max_selection_count = 3  # Her aracın en fazla kaç kez seçilebileceğini belirten sabit

    class Meta:
        unique_together = ['user', 'car_id']  # Her kullanıcı için aynı arabayı birden fazla kez seçememesini sağlar

    def save(self, *args, **kwargs):
        # Her seçim yapıldığında seçim sayısını kontrol et
        if self.selection_count > self.max_selection_count:
            self.selection_count = self.max_selection_count
        super().save(*args, **kwargs)


class Tripson(models.Model):
    TRIP_TYPES = [
         ('one_way', 'One Way'),
         ('round_trip', 'Round Trip')
     ]
    trip_type = models.CharField(max_length=20, choices=TRIP_TYPES)
    date = models.DateTimeField()
    from_date = models.DateTimeField(null=True, blank=True)  # For round trips
    return_date = models.DateTimeField(null=True, blank=True)  # For round trips
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=500)
    number_of_people = models.IntegerField()
    number_of_cars = models.IntegerField()
    distance = models.TextField()  # Change FloatField to TextField
    price = models.TextField()     # Change FloatField to TextField
    vehicle_id = models.CharField(max_length=100, null=True, blank=True)  # Added vehicle_id field
    email = models.EmailField(default='example@example.com')  # Added email field
    phone = models.CharField(max_length=20,default='(+90)511-111-11-11')  # Added phone field

    def _str_(self):
        return f"Trip from {self.origin} to {self.destination}"

class Trip(models.Model):
    TRIP_TYPES = [
         ('one_way', 'One Way'),
         ('round_trip', 'Round Trip')
     ]

    trip_type = models.CharField(max_length=20, choices=TRIP_TYPES)
    date = models.DateTimeField()
    from_date = models.DateTimeField(null=True, blank=True)  # For round trips
    return_date = models.DateTimeField(null=True, blank=True)  # For round trips
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    number_of_cars = models.IntegerField()
    distance = models.FloatField()
    price = models.FloatField()
    

    def _str_(self):
        return f"Trip from {self.origin} to {self.destination}"

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Diğer gerekli alanlar eklenebilir

    def str(self):
        return self.name




class DistancePriceData(models.Model):
    date = models.DateTimeField()
    from_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    number_of_cars = models.IntegerField()
    distance = models.FloatField()
    price = models.FloatField()

    def _str_(self):
        return f"Trip from {self.origin} to {self.destination}"



class Trip(models.Model):
    TRIP_TYPES = [
         ('one_way', 'One Way'),
         ('round_trip', 'Round Trip')
     ]

    trip_type = models.CharField(max_length=20, choices=TRIP_TYPES)
    date = models.DateTimeField()
    from_date = models.DateTimeField(null=True, blank=True)  # For round trips
    return_date = models.DateTimeField(null=True, blank=True)  # For round trips
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    number_of_cars = models.IntegerField()
    distance = models.FloatField()
    price = models.FloatField()
    

    def _str_(self):
        return f"Trip from {self.origin} to {self.destination}"




class Signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username
    class Meta:
        db_table = 'users'

class PriceCoefficient(models.Model):
    km_price_coefficient = models.FloatField(default=1.4)
    flat_rate_coefficient = models.FloatField(default=2)

    def _str_(self):
        return "Price Coefficients"