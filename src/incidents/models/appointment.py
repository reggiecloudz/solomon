from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Client, Technician
from incidents.models import SupportRequest

class Appointment(models.Model):
    label = models.CharField(_("label"), max_length=75, null=False, blank=True)
    appointment_date = models.DateTimeField(_("appointment date"), null=True, blank=True)
    was_accepted = models.BooleanField(_("was accepted"), default=False, null=False, blank=True)
    support_request = models.ForeignKey(SupportRequest, on_delete=models.CASCADE, related_name="support_requests", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("appointment")
        verbose_name_plural = _("appointments")

    def __str__(self):
        return f"{self.label}: {self.support_request.client.identity.name} appoinment"

    def get_absolute_url(self):
        return reverse("appointment_detail", kwargs={"pk": self.pk})
