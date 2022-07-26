from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from accounts.models import Client

class Device(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    computer_type = models.CharField(max_length=144, null=False, blank=True)
    peripherals = models.JSONField(default=list, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
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

    @property
    def open_requests(self):
        return self.support_requests.filter(is_open=True).count()

    @property
    def request_count(self):
        return self.support_requests.count()