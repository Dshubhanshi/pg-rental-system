from django import forms
from django.contrib.auth import authenticate, get_user_model

from .models import Review, Booking, ContactUs, CheckAvailability, Owner

User = get_user_model()

COMFORT_CHOICES = (
    ('low', 'Low'),
    ('sufficient', 'Sufficient'),
    ('good', 'Good'),
    ('excellent', 'Excellent'),
    ('super', 'Super'),
    ('i dont know', 'I dont know'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

SHARING_CHOICES = [
    ('yes', 'Yes'), 
    ('no', 'No'),
]

class ReviewForm(forms.ModelForm):
    comfort = forms.ChoiceField(choices=COMFORT_CHOICES)
    cost = forms.ChoiceField(choices=COMFORT_CHOICES)
    quality = forms.ChoiceField(choices=COMFORT_CHOICES)

    class Meta:
        model = Review
        fields = ['fname', 'lname', 'email', 'pg_type', 'comfort', 'cost', 'quality']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['fname', 'lname', 'email', 'contact', 'message']

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = CheckAvailability
        fields = ['name', 'pg_type', 'available_from', 'available_to', 'no_of_person', 'area', 'email']
        widgets = {'available_from': forms.DateInput(attrs={'type':'date'})}

class BookingForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    sharing = forms.ChoiceField(choices=SHARING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'pg_type', 'no_of_person', 
                  'arrival_date', 'departure_date', 'gender', 'sharing']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super().clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class OwnerForm(forms.ModelForm):
    sharing = forms.ChoiceField(choices=SHARING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Owner
        fields = ['name', 'contact', 'email', 'pg_type', 'description', 'price', 'sharing',
                  'wifi', 'laundry', 'food', 'maid', 'image']
