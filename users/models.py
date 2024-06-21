from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils import timezone
# class User(AbstractUser):
#     mobile_number = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(null=True, blank=True)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

#     def __str__(self):
#         return self.email
class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField('mobile number', 
                              max_length=10, 
                              unique=True, 
                              null=True, 
                              blank=True,
                              help_text='Enter Indian mobile number (e.g : 7207300602)'
                              )
    address = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return f"{self.name}"

class Task(models.Model):
    STATUS_PENDING = "Pending"
    STATUS_IN_PROGRESS = "In Progress"
    STATUS_COMPLETED = "Completed"

    STATUS_CHOICES = (
        ('STATUS_PENDING', 'STATUS_PENDING'),
        ('STATUS_IN_PROGRESS', 'STATUS_IN_PROGRESS'),
        ('STATUS_COMPLETED', 'STATUS_COMPLETED'),
    )
    name = models.CharField(max_length=255,blank=True, null=True)
    date_time = models.DateTimeField(default=timezone.now ,blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned',blank=True, null=True)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created',blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending',blank=True, null=True)

    def __str__(self):
        return self.name
