from hashlib import blake2b
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
import uuid

class AppUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_("name"), max_length=255, null=False, blank=True)
    is_client = models.BooleanField(default=False, blank=True)
    is_technician = models.BooleanField(default=False, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = AppUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-id"]

class Client(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    identity = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return self.identity.name

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})

class Technician(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    identity = models.OneToOneField(User, on_delete=models.CASCADE, related_name="technician", null=False, blank=True)
    # [{'service', 'rate',}]
    # Technician.objects.filter(service_rates__contains=[{'service': 'System updates'}])
    service_rates = models.JSONField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("technician")
        verbose_name_plural = _("technicians")

    def __str__(self):
        return self.identity.name

    def get_absolute_url(self):
        return reverse("technician_detail", kwargs={"pk": self.pk})
