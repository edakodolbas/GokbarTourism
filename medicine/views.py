import psycopg2
import logging

# Get a logger instance
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from .forms import SignupForm
from django. forms import inlineformset_factory
from .models import Signup
from .models import Trip
from medicine.models import Trip

from .forms import CreateUserForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .forms import ResetPasswordForm

from django.views.decorators.csrf import csrf_exempt
logger = logging.getLogger(__name__)



from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail
from django.conf import settings
from .models import PriceCoefficient
from django.shortcuts import render, redirect
from .forms import TripForm

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import DistancePriceData
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from .forms import TripsonForm

from .models import Trip
from .forms import TripsonForm

from .forms import LocationForm
from .models import Location

from .forms import CarSelectionForm

from .forms import TripsonForm
from django.core.mail import send_mail

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

def all_confirm(request):
    if request.method == 'POST':
        form = TripsonForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Form saved successfully")
            return redirect('success')  # Redirect to success page after successful form submission
        else:
            logger.error("Form is invalid: %s", form.errors)
    else:
        form = TripsonForm()
    
    context = {'form': form}
    return render(request, 'allconfirm.html', context)



from django.shortcuts import redirect

def allconfirm_tr_view(request):
    if request.method == 'POST':
        form = TripsonForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Form Başarıyla Kaydedildi")
            # return redirect('success_tr')  # Redirect to success_tr after successful form submission
            return redirect('success_tr')
        else:
            logger.error("Form Geçersiz: %s", form.errors)
    else:
        form = TripsonForm()
    
    context = {'form': form}
    return render(request, 'allconfirm_tr.html', context)






@csrf_exempt  # You may need to exempt this view from CSRF protection if you're facing CSRF errors
def send_reservation_email(request):
    if request.method == 'POST':
        # Extract form data from the request
        date = request.POST.get('date')
        return_date = request.POST.get('return_date')
        from_date = request.POST.get('from_date')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        trip_type = request.POST.get('trip_type')
        number_of_people = request.POST.get('number_of_people')
        number_of_cars = request.POST.get('number_of_cars')
        distance = request.POST.get('distance')
        price = request.POST.get('price')
        vehicle_id = request.POST.get('vehicle_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Prepare email content using the reservation_email.html template
        email_content = render_to_string('reservation_email.html', {
            'date': date,
            'return_date': return_date,
            'from_date': from_date,
            'origin': origin,
            'destination': destination,
            'trip_type': trip_type,
            'number_of_people': number_of_people,
            'number_of_cars': number_of_cars,
            'distance': distance,
            'price': price,
            'vehicle_id': vehicle_id,
            'email': email,
            'phone': phone,
        })

        # Send the email
        send_mail(
            subject='Reservation Confirmation',
            message='',  # You can leave this empty since you're sending HTML email
            html_message=email_content,
            from_email='reservation@gokbartourism.com',
            recipient_list=[email],
            fail_silently=False,
        )

        # Return a success response
        return HttpResponse('Email sent successfully!')
    else:
        # If the request method is not POST, return an error response
        return HttpResponse('POST requests are only supported.')









def vehicles_view(request):
    if request.method == 'POST':
        form = CarSelectionForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data['car_id']
            user = request.user
            # Kullanıcının seçtiği aracı SelectedCar modeline kaydet
            selected_car, created = SelectedCar.objects.get_or_create(user=user, car_id=car_id)
            # Seçilen aracı daha önce seçilmişse, selection_count alanını arttır
            if not created:
                selected_car.selection_count += 1
                selected_car.save()
            return render(request, 'success.html')  # Başarı sayfasına yönlendirme yapabilirsiniz
    else:
        form = CarSelectionForm()
    return render(request, 'vehicles.html', {'form': form})




def vehicles_tr_view(request):
    if request.method == 'POST':
        form = CarSelectionForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data['car_id']
            user = request.user
            # Kullanıcının seçtiği aracı SelectedCar modeline kaydet
            selected_car, created = SelectedCar.objects.get_or_create(user=user, car_id=car_id)
            # Seçilen aracı daha önce seçilmişse, selection_count alanını arttır
            if not created:
                selected_car.selection_count += 1
                selected_car.save()
            return render(request, 'success.html')  # Başarı sayfasına yönlendirme yapabilirsiniz
    else:
        form = CarSelectionForm()
    return render(request, 'vehicles_tr.html', {'form': form})









def vehicle_list(request):
    cars = Car.objects.all()
    return render(request, 'vehicles.html', {'cars': cars})



def map_view(request):
    form = LocationForm(request.POST or None)
    locations = Location.objects.all()  # mevcut konumlar

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('map_view')

    return render(request, 'map.html', {'form': form, 'locations': locations})

def hesapla(request):
    submitted=False
    if request.method == "POST":
        form=TripsonForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/hesapla?submitted=True')
    else:
        form=TripsonForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,'hesapla.html',{'form': form,'submitted': submitted})



def save_trip_data(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)






def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            # Başka bir sayfaya yönlendirme veya işlem tamamlandıktan sonra başka bir şey yapabilirsiniz
    else:
        form = TripForm()
    return render(request, 'create_trip.html', {'form': form})

def trip_view(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')  # Redirect to payment page after successful form submission
    else:
        form = TripForm()
    context = {'form': form}
    return render(request, 'distance_price.html', context)

@csrf_exempt
def save_trip(request):
    if request.method == 'POST':
        # AJAX isteğinden verileri al
        date = request.POST.get('date')
        return_date = request.POST.get('return_date')
        from_date = request.POST.get('from_date')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        number_of_people = request.POST.get('number_of_people')
        number_of_cars = request.POST.get('number_of_cars')
        price = request.POST.get('price')
        distance = request.POST.get('distance')
        trip_type = request.POST.get('trip_type')

        # Veritabanına kaydet
        trip_instance = Trip.objects.create(
            date=date,
            return_date=return_date,
            from_date=from_date,
            origin=origin,
            destination=destination,
            number_of_people=number_of_people,
            number_of_cars=number_of_cars,
            price=price,
            distance=distance,
            trip_type=trip_type
        )

        # Başarılı bir şekilde kaydedildiğine dair JSON yanıtı gönder
        return JsonResponse({'success': True})
    else:
        # Hatalı istek durumunda uygun JSON yanıtı gönder
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def edit_trip(request, pk):
    if request.method == 'POST':
        # İlgili model örneğini al
        trip_instance = get_object_or_404(Trip, pk=pk)

        # AJAX isteğinden verileri al
        trip_instance.date = request.POST.get('date')
        trip_instance.return_date = request.POST.get('return_date')
        trip_instance.from_date = request.POST.get('from_date')
        trip_instance.origin = request.POST.get('origin')
        trip_instance.destination = request.POST.get('destination')
        trip_instance.number_of_people = request.POST.get('number_of_people')
        trip_instance.number_of_cars = request.POST.get('number_of_cars')
        trip_instance.price = request.POST.get('price')
        trip_instance.distance = request.POST.get('distance')
        trip_instance.trip_type = request.POST.get('trip_type')

        # Veritabanına kaydet
        trip_instance.save()

        return JsonResponse({'success': True})  # Başarılı bir şekilde güncellendiğine dair JSON yanıtı gönder

def book_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')  # Başarılı bir şekilde form kaydedildikten sonra yönlendirme yap
    else:
        form = TripForm()
    return render(request, 'distance_price.html', {'form': form})

def fetch_coefficients(request):
    coefficients = PriceCoefficient.objects.first()
    data = {
        'km_price_coefficient': coefficients.km_price_coefficient,
        'flat_rate_coefficient': coefficients.flat_rate_coefficient,
    }
    return JsonResponse(data)

def homepage(request):
    signup=Signup.objects.all()
    return render(request, 'index.html', {'signups': signup})

def index_tr_view(request):
    signup=Signup.objects.all()
    return render(request, 'index_tr.html', {'signups': signup})   

def signup_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'signup.html', context)

def signup_tr_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'signup_tr.html', context)    

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            confirm_new_password = form.cleaned_data.get('confirm_new_password')
            
            # Parola doğrulama işlemleri
            if new_password == confirm_new_password:
                # Burada parolanın veritabanına kaydedilmesi işlemi gerçekleştirilir.
                # Bu örnek uygulamada parolalar doğrudan veritabanına kaydedilmiyor.
                # Burada sadece başarılı mesajı gönderilir.
                messages.success(request, 'Your password has been reset successfully!')
                return redirect('reset_password')  # Reset password sayfasına yeniden yönlendirme
            else:
                messages.error(request, 'Passwords do not match. Please try again.')
                return redirect('reset_password')
    else:
        form = ResetPasswordForm()
    
    return render(request, 'reset_password.html', {'form': form})
def forget_password(request):
    # Your view logic here
    return render(request, 'forget_password.html', {})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')   # Redirect to the homepage after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def login_tr_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')   # Redirect to the homepage after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login_tr.html', {'form': form})    

def confirm_view(request):
    if request.method == 'POST':
        # Handle form submission if needed
        pass
    else:
        signup_info = Signup.objects.last()  # Get the latest signup info
        reservations = Reservation.objects.all()  # Get all reservations
    return render(request, 'confirm.html', {'signup_info': signup_info, 'reservations': reservations})

def contact_view(request):
    return render(request, "contact.html")
def contact_tr_view(request):
    return render(request, "contact_tr.html")    

def vehicles_view(request):
    return render(request, "vehicles.html")

def distance_price_view(request):
    return render(request, "distance_price.html")

def payment_view(request):
    return render(request, "payment.html")


def payment_tr_view(request):
    return render(request, "payment_tr.html")

def save_distance_price(request):
    if request.method == 'POST':
        # Extract data from the POST request
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        distance = request.POST.get('distance')
        price = request.POST.get('price')
        print('Received POST request for saving distance and price') 
      
        # Save the data to your database or perform any other action
        # Example: Saving to a model
        # Trip.objects.create(from_location=from_location, to_location=to_location, distance=distance, price=price)
        
        # Return a JSON response indicating success
        return JsonResponse({'message': 'Data saved successfully'}, status=200)
    else:
        # Return a JSON response indicating failure
        return JsonResponse({'message': 'Invalid request method'}, status=400)




def confirm_view(request):
    if request.method == 'POST':
        # Handle form submission if needed
        pass
    else:
        signup_info = Signup.objects.last()  # Get the latest signup info
        reservations = Reservation.objects.all()  # Get all reservations
    return render(request, 'confirm.html', {'signup_info': signup_info, 'reservations': reservations})


def contact_view(request):
    return render(request, "contact.html")

def get_address(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    
    # Burada Esri Geocoding Plugin'i ile koordinatları adres bilgisine dönüştürüyoruz.
    # Dönen adres bilgisini JSON formatında HttpResponse olarak gönderiyoruz.
    address = geocode(lat, lng)  # Geocode fonksiyonu Esri Geocoding Plugin'i ile koordinatları adres bilgisine dönüştürür
    return JsonResponse({'address': address})

# Esri Geocoding Plugin'ini kullanarak koordinatları adres bilgisine dönüştüren bir fonksiyon
def geocode(lat, lng):
    # Burada Esri Geocoding Plugin'i kullanarak koordinatları adres bilgisine dönüştürüyoruz
    # Dönüştürülen adres bilgisini döndürüyoruz
    return converted_address

    from .forms import TripForm

def trip_view(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip_type = form.cleaned_data['trip_type']
            date = form.cleaned_data['date']
            from_address = form.cleaned_data['from_address']
            to_address = form.cleaned_data['to_address']
            number_of_people = form.cleaned_data['number_of_people']
            number_of_cars = form.cleaned_data['number_of_cars']
            # Diğer işlemleri buraya ekleyebilirsiniz
            return render(request, 'result.html', {'trip_type': trip_type, 'date': date, 'from_address': from_address, 'to_address': to_address, 'number_of_people': number_of_people, 'number_of_cars': number_of_cars})
    else:
        form = TripForm()
    return render(request, 'trip_form.html', {'form': form})

    from django.shortcuts import render

# views.py

from django.shortcuts import render
from .forms import CarSelectionForm
from .models import SelectedCar

def vehicles_view(request):
    if request.method == 'POST':
        form = CarSelectionForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data['car_id']
            # Burada seçilen aracı Django veritabanına kaydedebilirsiniz
            # Örnek olarak:
            SelectedCar.objects.create(user=request.user, car_id=car_id)  # user'e giriş yapan kullanıcının bilgisi eklenmeli
            return render(request, 'success.html')  # Başarı sayfasına yönlendirme yapabilirsiniz
    else:
        form = CarSelectionForm()
    return render(request, 'vehicles.html', {'form': form})

    # views.py

from django.shortcuts import render, redirect
from .forms import CarSelectionForm
from .models import SelectedCar

def vehicles_view(request):
    if request.method == 'POST':
        form = CarSelectionForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data['car_id']
            user = request.user
            
            # Kullanıcının seçtiği aracı belirle
            selected_cars_count = SelectedCar.objects.filter(user=user, car_id=car_id).count()
            
            # Aynı aracı en fazla 3 kez seçmesine izin ver
            if selected_cars_count < 3:
                SelectedCar.objects.create(user=user, car_id=car_id)
            
            return redirect('success')  # Başarı sayfasına yönlendirme yapabilirsiniz
    else:
        form = CarSelectionForm()
    return render(request, 'vehicles.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def success_tr_view(request):
    return render(request, 'success_tr.html')    