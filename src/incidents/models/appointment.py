from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Job

class Appointment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="appointments", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("appointment")
        verbose_name_plural = _("appointments")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("appointment_detail", kwargs={"pk": self.pk})
