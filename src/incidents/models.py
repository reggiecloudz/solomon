from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from assets.models import Device

from .choices import INCIDENT_STATUS_CHOICES
from accounts.models import Client, Technician

class Incident(models.Model):
    subject = models.CharField(max_length=144, null=False, blank=True)
    explanation = models.TextField(null=False, blank=True)
    status = models.CharField(max_length=60, default="Submitted", choices=INCIDENT_STATUS_CHOICES, null=False, blank=True)
    start_date = models.DateField(null=True, blank=True)
    resolved_date = models.DateField(null=True, blank=True)
    start_work_time = models.TimeField(null=True, blank=True)
    end_work_time = models.TimeField(null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="incidents", null=False, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="incidents", null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, related_name="incidents", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("incident")
        verbose_name_plural = _("incidents")

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("incident_detail", kwargs={"pk": self.pk})
