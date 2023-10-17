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
