from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Client, Technician
from assets.models import Device
from incidents.choices import SUPPORT_REQUEST_STATUS_CHOICES
from questions.models import Questionnaire

class SupportRequest(models.Model):
    problem = models.TextField(_("problem"), null=False, blank=True)
    details = models.TextField(_("details"), null=True, blank=True)
    is_open = models.BooleanField(_("is open"), default=True, null=False, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='support_requests', null=False, blank=True)
    # { hourly_rate: 22, scheduled_start_date: date, services: [], summary: "", agreed: false, comments: ""}
    offer = models.JSONField(default=dict, null=True, blank=True)
    # date, action
    followup_dates = models.JSONField(default=list, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='support_requests', null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, related_name="support_requests", null=True, blank=True)
    questionnaire = models.OneToOneField(Questionnaire, on_delete=models.SET_NULL, related_name='support_request', null=True, blank=True)
    status = models.CharField(_("status"), max_length=50, choices=SUPPORT_REQUEST_STATUS_CHOICES, default="Submitted", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("support request")
        verbose_name_plural = _("support requests")

    def __str__(self):
        return f"{self.client.identity.name}'s support request for {self.created}"

    def get_absolute_url(self):
        return reverse("support_request_detail", kwargs={"pk": self.pk})
