from email.policy import default
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Technician
from incidents.models import ServiceOrder
from incidents.choices import PRIORITY_CHOICES, JOB_STATUS_CHOICES

class Job(models.Model):
    label = models.CharField(_("label"), max_length=75, null=False, blank=True)
    priority = models.CharField(_("priority"), choices=PRIORITY_CHOICES, max_length=20, null=False, blank=True)
    status = models.CharField(_("status"), choices=JOB_STATUS_CHOICES, default="Created", max_length=20, null=False, blank=True)
    queue = models.PositiveIntegerField(_("queue"), default=0, null=False, blank=True)
    # update this field when from the value of the time between work periods
    hours_worked = models.FloatField(_("hours worked"), default=0.0, null=False, blank=True)
    service_order = models.OneToOneField(ServiceOrder, on_delete=models.CASCADE, related_name="job", null=False, blank=True)
    # resource, url, title, description
    documentation = models.JSONField(default=list, null=True, blank=True)
    # [started, paused (timestamps), last_url] ref forplay
    work_periods = models.JSONField(_("work periods"), default=list, null=True, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name="jobs", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("job")
        verbose_name_plural = _("jobs")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"pk": self.pk})
