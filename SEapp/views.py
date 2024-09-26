from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserLoginForm, UserRegisterForm, ReviewForm, BookingForm, ContactForm, AvailabilityForm
from .models import Review, Booking, FacilitiesPrice, CheckAvailability, Owner, Payment, Photo

# Single definitions are used to render templates
def home(request):
    user=request.user
    return render(request, 'index2.html', {'user':user})
def dashboard(request):
    user=request.user.id
    print(user)
    bookings=Booking.objects.filter(id=user)
    print(bookings)
    return render(request, 'dashboard.html' , {'bookings':bookings})
def blog(request):
    return render(request, "blog.html", {})

def faq(request):
    return render(request, "faq.html", {})

def room_detail(request):
    return render(request, "room_detail/room_detail.html", {})

def room_detail1(request):
    return render(request, "room_detail/room_detail1.html", {})

def room_detail2(request):
    return render(request, "room_detail/room_detail2.html", {})

def room_detail3(request):
    return render(request, "room_detail/room_detail3.html", {})

def about(request):
    return render(request, "about.html", {})

def gallery(request):
    return render(request, "gallery.html", {})

def booking_success(request):
    return render(request, "booking/booking_confirmation.html", {})

def booking_detail(request):
    return render(request, "booking/booking_detail.html", {})

def review_list(request):
    """
    This method is basically for searching reviews of all the PGs.
    :param request: url of the review list
    :return: template with context
    """
    #get the searching query
    search = request.GET.get("q", None)
    #get all objects from review model
    qs = Review.objects.all()
    if search is not None:
        #filter the data
        qs = qs.filter(
            Q(pg_type__icontains=search) |
            Q(comfort__icontains=search) |
            Q(cost__icontains=search) |
            Q(quality__icontains=search)
            )
    context = {
            'object_list': qs
    }
    template = "review/review_list.html"
    return render(request, template, context)

def review_list1(request):
    """
        This method is basically for searching reviews of 1* the PGs.
        :return: template with context
        """
    qs = Review.objects.all()
    qs = qs.filter(
        Q(pg_type__icontains="1*")
        )
    context = {
            'object_list': qs
    }
    template = "review/review_list.html"
    return render(request, template, context)

def review_list2(request):
    """
        This method is basically for searching reviews of 2* the PGs.
        :return: template with context
        """
    qs = Review.objects.all()
    qs = qs.filter(
        Q(pg_type__icontains="2*")
        )
    context = {
            'object_list': qs
    }
    template = "review/review_list.html"
    return render(request, template, context)

def review_list3(request):
    """
        This method is basically for searching reviews of 3* the PGs.
        :return: template with context
        """
    qs = Review.objects.all()
    qs = qs.filter(
        Q(pg_type__icontains="3*")
        )
    context = {
            'object_list': qs
    }
    template = "review/review_list.html"
    return render(request, template, context)

def review_list4(request):
    """
    This method is basically for searching reviews of 4* the PGs.
    :return: template with context
    """
    qs = Review.objects.all()
    qs = qs.filter(
        Q(pg_type__icontains="4*")
        )
    context = {
            'object_list': qs
    }
    template = "review/review_list.html"
    return render(request, template, context)

def room_details(request, id=None):
    """
    This method is to display 1* PG's room details
    :param id: id of the record
    :return: template with context
    """
    pg_type = "1*"
    qs = Owner.objects.all()
    #get all the images from photo model
    photo = Photo.objects.all()
    qs = Owner.objects.all()
    #filter for 2* pg
    qs = qs.filter(
        Q(pg_type__icontains=pg_type)
    )
    i = 0
    #to get all the images
    while (i < len(qs.values())):
        photo_name = qs.values()[i]['id']
        images = Photo.objects.filter(photo=photo_name)
        i += 1
    context = {
            'object_list': qs,
            'photos': photo,
            'images': images,
            'room_id':photo_name,
    }
    template = "room_detail/room_detail.html"
    return render(request, template, context)

def room_detail1(request, id=None):
    """
        This method is to display 1* PG's room details
        :param id: id of the record
        :return: template with context
        """
    pg_type = "2*"
    #get all the images from photo model
    photo = Photo.objects.all()
    qs = Owner.objects.all()
    #filter for 2* pg
    qs = qs.filter(
        Q(pg_type__icontains=pg_type)
    )
    i = 0
    #to get all the images
    while (i < len(qs.values())):
        photo_name = qs.values()[i]['id']
        images = Photo.objects.filter(photo=photo_name)
        i += 1
    context = {
            'object_list': qs,
            'photos': photo,
            'images': images,
            'room_id':photo_name,
    }
    template = "room_detail/room_detail1.html"
    return render(request, template, context)

def room_detail2(request, id=None):
    pg_type = "3*"
    photo = Photo.objects.all()
    qs = Owner.objects.all()
    qs = qs.filter(
        Q(pg_type__icontains=pg_type)
    )
    
    images = []
    photo_name = None  # Initialize photo_name variable
    
    for owner in qs:
        photo_name = owner.id
        owner_images = Photo.objects.filter(photo=photo_name)
        images.extend(owner_images)
    
    context = {
        'object_list': qs,
        'photos': photo,
        'images': images,
        'room_id': photo_name,  # Assign photo_name outside the loop
    }
    
    template = "room_detail/room_detail2.html"
    return render(request, template, context)



def room_detail3(request, id=None):
    pg_type = "4*"
    #get all the images from photo model
    photo = Photo.objects.all()
    qs = Owner.objects.all()
    #filter for 2* pg
    qs = qs.filter(
        Q(pg_type__icontains=pg_type)
    )
    i = 0
    #to get all the images
    while (i < len(qs.values())):
        photo_name = qs.values()[i]['id']
        images = Photo.objects.filter(photo=photo_name)
        i += 1
    context = {
            'object_list': qs,
            'photos': photo,
            'images': images,
            'room_id':photo_name,
    }
    template = "room_detail/room_detail3.html"
    return render(request, template, context)

@login_required(login_url='/login/')
def review_create(request):
    request_path = request.get_full_path()
    next = request.GET.get('next')
    title = "Review"
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/review_list")
    return render(request, "review/review_create.html", {"form":form, "title": title, 'req': request_path})

def login_view(request):
    """
    This method is for user login.
    """
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", {"form":form, "title": title})

def register_view(request):
    """
    This method is for user registration.
    """
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)

def check_availibility(request):
    """
    This method checks the room availability.
    """
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data.get('name')
            form_email = form.cleaned_data.get("email")
            subject = 'Availability Form'
            from_email = settings.EMAIL_HOST_USER
            some_html_message = """
            <h2>This is an Availability form. Contact the owner by using contact number</h2>
            """
            
               
            pg_type = form.cleaned_data.get('pg_type')
            available_from = form.cleaned_data.get('available_from')
            available_to = form.cleaned_data.get('available_to')
            no_of_person = form.cleaned_data.get('no_of_person')
            area = form.cleaned_data.get('area')
            print(f"{pg_type}-------------{available_from}-------{available_to}------{area}----")

            check_availibility =CheckAvailability.objects.filter(pg_type=pg_type,available_from__lte = available_from ,available_to__gte =available_to,area=area )
            print(check_availibility)
            if check_availibility.exists():
                return render (request, 'checking_res.html',{'availabilities':check_availibility})
            else:
                return HttpResponse("<h1> Room is not available </h1>")   

    else:
        form = AvailabilityForm()

    context = {
        'form': form
    }
    return render(request, 'check_availibility.html', context)


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import FacilitiesPrice, Booking
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import BookingForm  # Import your BookingForm from forms.py
@login_required(login_url='/login/')
def booking(request):
    title = "Book Your Room"
    form = BookingForm(request.POST or None)
    
    if form.is_valid():
        obj = form.save(commit=False)
        
        # Price calculation logic (uncomment and update as needed)
        # price = calculate_price(form.cleaned_data)
        # obj.price = price
        
        obj.save()
        user_email = request.user.email
        send_mail(
            'Booking Confirmation',
            'Your booking has been confirmed through stayeasy website . For any booking update query or booking cancelation please contact at business.stayeasy.org@gmail.com',
            'business.stayeasy.org@gmail.com',
            [user_email],
            fail_silently=False,
        )
        
        
        # Redirect to a success page or booking detail page
        return render(request, 'sucesses.html')  # Redirect to booking detail page
    
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'form.html', context)

def booking_detail(request, id=None):
    """
    This method shows the booking details of user.
    """
    request.session['booking_id'] = id
    qs = get_object_or_404(Booking, id=id)
    context = {
        'object': qs
    }
    request.session['price'] = str(qs.price)    
    template = "booking/booking_detail.html"
    return render(request, template, context)

def payment_view(request, id=None):
    """
    This method is for payment view.
    """
    price = request.session.get('price')
    balance = Payment.objects.all()
    rem_balance = balance[0].rem_balance - float((price).decode('ascii'))
    updated_balance = Payment.objects.filter(id=1).update(rem_balance=rem_balance)
    template = "proceed_payment.html"
    context = {
            'price': price
    }
    return render(request, template, context)

def booking_update(request, id=None):
    """
    This method is for updating booking details.
    """
    qs = get_object_or_404(Booking, id=id)
    form = BookingForm(request.POST or None, instance=qs)
    context = {
            'object': qs,
            'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        price = 0
        wifi_status = form.cleaned_data.get('wifi')
        loundry_status = form.cleaned_data.get('loundry')
        food_status = form.cleaned_data.get('food')
        maid_status = form.cleaned_data.get('maid')
        if wifi_status == True:
            name =  FacilitiesPrice.objects.get(name='wifi')
            price += name.price
        if loundry_status == True:
            name =  FacilitiesPrice.objects.get(name='loundry')
            price += name.price
        if food_status == True:
            name =  FacilitiesPrice.objects.get(name='food')
            price += name.price
        if maid_status == True:
            name =  FacilitiesPrice.objects.get(name='maid')
            price += name.price
        pg_type = form.cleaned_data.get('pg_type')
        name = FacilitiesPrice.objects.get(name=pg_type)
        price += name.price
        price_obj = Booking.objects.filter(pg_type=name).update(price=price)
        return HttpResponseRedirect("/{num}".format(num=obj.id))
    template = 'booking/booking_update.html'
    return render(request, template, context)

def booking_delete(request, id=None):
    """
    This method deletes the booking.
    """
    obj = get_object_or_404(Booking, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    context = {
            'object': obj
    }
    template = "booking/booking_delete.html"
    return render(request, template, context)

def contact_us(request):
    """
    This method is for contact purpose.
    """
    user_email = request.user.email
    print(user_email,"=====================")
    next = request.GET.get('next')
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("fname")
        form_contact = form.cleaned_data.get("contact")
        subject = 'PG Enquiry Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = "%s: %s via %s"%( 
                form_full_name, 
                form_message, 
                form_contact)
        send_mail(
            subject,
            contact_message,
            settings.EMAIL_HOST_USER,
            to_email,
            fail_silently=False,
        )
        return HttpResponseRedirect("/")
    return render(request, "form.html", {"form":form, "title": title})

def logout_view(request):
    """
    This methos is for user logout.
    """
    logout(request)
    return redirect("/")

def bookingssss(request):
    if request.method=='POST':
        id=request.POST.get('pg_id')
        print(id,'===============================')
        return render(request,'booking-form.html')
