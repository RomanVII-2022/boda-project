from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class PersonnelManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, job_title, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number,
            job_title=job_title
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, job_title, password=None):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
            phone_number=phone_number,
            job_title=job_title
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Personnel(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=225)
    phone_number = PhoneNumberField()
    job_title = models.CharField(max_length=225)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = PersonnelManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "phone_number", "job_title"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    

Business_or_Person_Choices = [('Business', 'Business'), ('Individual', 'Individual')]


class Shipper(models.Model):
    full_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone_number = PhoneNumberField()
    business_or_person = models.CharField(max_length=225, choices=Business_or_Person_Choices, default='Business')
    password = models.CharField(max_length=225)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    

class Carrier(models.Model):
    email = models.EmailField(max_length=225)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=225)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=225)
    status = models.CharField(max_length=225, choices=[('Domant', 'Domant'), ('Onboarding', 'Onboarding'), ('Processing', 'Processing'), ('Active', 'Active'), ('Available', 'Available'), ('Engaged', 'Engaged'), ('Withdraw', 'Withdraw'), ('Suspended', 'Suspended'), ('Blacklisted', 'Blacklisted'), ('Archive', 'Archive')], default='Onboarding')
    national_id = models.CharField(max_length=225)
    national_id_document = models.FileField()
    driving_licence = models.FileField()
    good_conduct = models.FileField()
    kra_pin = models.FileField()
    defensive_driving_certificate = models.FileField()
    reference_letter_from_chief = models.FileField()
    profile_photo = models.ImageField(upload_to='profilePhotos')
    medical_report  = models.FileField()
    appointment_letter = models.FileField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.full_name
    

class VehicleType(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=225)
    insurance_certificate_number = models.CharField(max_length=225)
    Vehicle_model = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_photo = models.ImageField('vehicleProfiles')
    driver = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_number


class Order(models.Model):
    commodity = models.CharField(max_length=225)
    description = models.TextField()
    vehicle_type = models.CharField(max_length=225, choices=[('Motorcyle', 'Motorcycle'), ('TukTuk', 'TukTuk')], default='Motorcyle')
    pickup_location = models.CharField(max_length=225)
    pickup_date = models.DateTimeField()
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    dropoff_location = models.CharField(max_length=225)
    dropoff_contact_name = models.CharField(max_length=225)
    dropoff_phone_number = PhoneNumberField()
    dropoff_instruction = models.TextField()
    order_status = models.CharField(max_length=225, choices=[('Inprogress', 'Inprogress'), ('Upcoming', 'Upcoming'), ('Posted', 'Posted'), ('Cancelled', 'Cancelled')])
    payment_status = models.CharField(max_length=225)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commodity