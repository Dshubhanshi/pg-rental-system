

# Register your models here.
from django.contrib import admin
from .models import Booking, ContactUs, Review, FacilitiesPrice, CheckAvailability, Owner, Payment, Photo

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'pg_type', 'available_from', 'available_to', 'no_of_person', 'area', 'available']
    list_filter = ['pg_type', 'available_from', 'available_to', 'area', 'no_of_person']

class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'arrival_date', 'departure_date', 'gender', 'sharing', 'wifi', 'laundry', 'maid', 'food']
    list_filter = ['gender', 'arrival_date', 'departure_date']
    search_fields = ['gender']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'contact', 'message']
    search_fields = ['fname', 'contact']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'pg_type', 'comfort', 'cost', 'quality']
    search_fields = ['comfort', 'cost', 'quality', 'pg_type']
    list_filter = ['email', 'cost', 'quality', 'pg_type']

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'email', 'pg_type', 'description', 'price', 'sharing', 'wifi', 'laundry', 'food', 'maid']
    inlines = [PhotoInline]
    search_fields = ['pg_type']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['ac_no', 'ini_balance', 'rem_balance']

admin.site.register(Booking, BookingAdmin)
admin.site.register(ContactUs, ContactAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(FacilitiesPrice, FacilityAdmin)
admin.site.register(CheckAvailability, AvailabilityAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Payment, PaymentAdmin)

admin.site.site_title = "Stay Easy"
admin.site.site_header = "Stay Easy"
# admin.site.register(Booking)
# admin.site.register(CheckAvailability)