from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from SEapp.views import (login_view, register_view, logout_view, 
    booking, booking_success, contact_us, 
    review_create, booking_detail, check_availibility, 
    gallery, booking_detail, about, 
    blog, faq, room_detail, room_detail1, 
    room_detail2, room_detail3, payment_view,bookingssss,dashboard)

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include(('SEapp.urls', 'SEapp'), namespace='app')),
    path('accounts/', include('registration.backends.default.urls')),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check_availibility/', check_availibility, name='check_availibility'),
    path('booking/', booking, name='booking'),
    path('contact_us/', contact_us, name='contact_us'),
    path('review_create/', review_create, name='review_create'),
    path('checkout/', payment_view, name='checkout'),
    path('booking_success/', booking_success, name='booking_success'),
    path('logout/', logout_view, name='logout'),
    path('gallery/', gallery, name='gallery'),
    path('booking_detail/', booking_detail, name='booking_detail'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('faq/', faq, name='faq'),
    path('room_detail/', room_detail, name='room_detail'),
    path('room_detail1/', room_detail1, name='room_detail1'),
    path('room_detail2/', room_detail2, name='room_detail2'),
    path('room_detail3/', room_detail3, name='room_detail3'),
    path('check_availibility/', check_availibility, name='check_availibility'),
    path('bookingssss/',bookingssss,name="bookingssss"),
    path('dashboard/',dashboard, name="dashboard"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
