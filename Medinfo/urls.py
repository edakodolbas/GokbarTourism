"""
URL configuration for Medinfo project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path
from medicine import views 
from medicine.views import homepage, signup_view, login_view, confirm_view,contact_view,all_confirm,signup_tr_view,index_tr_view,login_tr_view,contact_tr_view,allconfirm_tr_view,payment_tr_view
from medicine.views import vehicles_view,payment_view,save_distance_price,distance_price_view,save_trip_data,map_view,vehicle_list,save_trip_data,all_confirm, trip_view, vehicles_view,vehicles_tr_view
from medicine.views import vehicles_view, success_view,send_reservation_email,success_tr_view
from django.conf.urls.static import static
urlpatterns = [


    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup.html', views.signup_view, name='signup_html'),
    path('signup/', views.signup_view, name='signup'),
    path('login.html', views.login_view, name='login_html'),
    path('distance_price.html', views.distance_price_view, name='distance_price_html'),
    path('payment.html', views.payment_view, name='payment_html'),  # Directly serving the payment.html file
    path('map/', views.map_view, name='map_view'),

    path('allconfirm/', views.all_confirm, name='all_confirm'),
    path('allconfirm_tr/', views.allconfirm_tr_view, name='allconfirm_tr'),  # Update to use 'allconfirm_tr_view'

    path('vehicles.html', views.vehicles_view, name='vehicles_html'),
    path('confirm/', views.confirm_view, name='confirm'),
    path('save-distance-price/', views.save_distance_price, name='save_distance_price'),
    path('fetch-coefficients/', views.fetch_coefficients, name='fetch_coefficients'),
    path('contact.html', views.contact_view, name='contact_html'),
    path('save-distance-price/', views.save_distance_price, name='save_distance_price'),
    path('book-trip/', views.book_trip, name='book_trip'),
    path('hesapla/', views.hesapla, name='hesapla'),

    path('allconfirm.html', views.all_confirm, name='all_confirm_html'),  # Remove this line if 'allconfirm_tr_view' serves the same purpose
    path('allconfirm_tr.html', views.allconfirm_tr_view, name='allconfirm_tr_html'),

    path('hesapla.html', views.hesapla, name='hesapla_html'),  
    path('save-trip-data/', views.save_trip_data, name='save_trip_data'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('get_address/', views.get_address, name='get_address'),
    path('trip/', views.trip_view, name='trip_view'),
    path('forget_password.html', views.forget_password, name='forget_password'),
    path('send-reservation-email/', views.send_reservation_email, name='send_reservation_email'),
    path('payment/', views.payment_view, name='payment'),
    path('success/', views.success_view, name='success'),
    path('success_tr/', views.success_tr_view, name='success_tr'),
    path('signup_tr.html', views.signup_tr_view, name='signup_tr_html'),
    path('signup_tr/', views.signup_tr_view, name='signup_tr'),
    path('index_tr.html', views.index_tr_view, name='index_tr_html'),
    path('login_tr.html', views.login_tr_view, name='login_tr_html'),
    path('contact_tr.html', views.contact_tr_view, name='contact_tr_html'),
    path('payment_tr.html', views.payment_tr_view, name='payment_tr_html'),
    path('vehicles_tr/', views.vehicles_tr_view, name='vehicles_tr_html'),
    path('vehicles_tr.html', views.vehicles_tr_view, name='vehicles_tr_html'),
    path('success/payment.html', views.payment_view, name='payment_html'),
    path('success_tr/payment_tr.html', views.payment_tr_view, name='payment_tr'),

    # path('all_confirm_tr.html', views.allconfirm_tr_view, name='all_confirm_tr_html'),  # Make sure this line is correct, not duplicated

    path('success_tr/', views.success_tr_view, name='success_tr'),
    path('payment_tr/', views.payment_tr_view, name='payment_tr'),



    #path('make-reservation/', views.make_reservation, name='make_reservation'),
]