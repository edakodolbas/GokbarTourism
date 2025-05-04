from .models import Signup
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Trip

from django import forms
from .models import Trip
from .models import Tripson
from .models import DistancePriceData

from .models import Location




class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude']

class TripsonForm(forms.ModelForm):
    class Meta:
        model=Tripson
        fields="__all__"

def calculate_distance_and_price(request):
    submitted = False
    if request.method == "POST":
        form = DistancePriceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/calculate_distance_and_price?submitted=True')
    else:
        form = DistancePriceForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'distance_price.html', {'form': form, 'submitted': submitted})


class DistancePriceForm(forms.ModelForm):
    class Meta:
        model = DistancePriceData
        fields = "__all__"       



class TripForm(forms.Form):
    trip_type = forms.ChoiceField(choices=[('oneWay', 'One Way'), ('roundTrip', 'Round Trip')])
    date = forms.DateTimeField(required=False)
    from_address = forms.CharField(max_length=100)
    to_address = forms.CharField(max_length=100)
    number_of_people = forms.IntegerField(min_value=1, max_value=15)
    number_of_cars = forms.IntegerField(min_value=1, max_value=5)



class CarSelectionForm(forms.Form):
    car_id = forms.IntegerField()




class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['trip_type', 'date', 'from_date', 'return_date', 'origin', 'destination', 'number_of_people', 'number_of_cars']

 

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    show_password = forms.BooleanField(label='Show Password', required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

   
        if new_password != confirm_new_password:
            raise forms.ValidationError("The new passwords do not match.")

        return cleaned_data
        
class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']

# Remove the following line
# admin.site.register(User, UserAdmin)