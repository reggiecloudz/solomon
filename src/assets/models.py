from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from accounts.models import Client

class Device(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    operating_system = models.CharField(max_length=64, null=False, blank=True)
    about = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devices', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("device")
        verbose_name_plural = _("devices")

    def __str__(self):
        return f"{self.client.identity.name}'s {self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("device_detail", kwargs={"pk": self.pk})

class Part(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    incident = models.ForeignKey('incidents.Incident', on_delete=models.CASCADE, related_name='parts', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("part")
        verbose_name_plural = _("parts")

    def __str__(self):
        return f"{self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("part_detail", kwargs={"pk": self.pk})
