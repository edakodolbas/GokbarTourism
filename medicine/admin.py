from django.contrib import admin
from .models import Signup
from .models import PriceCoefficient
# from .models import Trip
from .models import Tripson
from .models import DistancePriceData

from .models import Location
from .models import SelectedCar


admin.site.register(PriceCoefficient)

admin.site.register(Signup)
# admin.site.register(Trip)
admin.site.register(Tripson)
admin.site.register(DistancePriceData)

admin.site.register(SelectedCar)



class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_type', 'date', 'from_address', 'to_address', 'number_of_people', 'number_of_cars')
    list_filter = ('trip_type', 'date')
    search_fields = ('from_address', 'to_address')
    # admin.py





