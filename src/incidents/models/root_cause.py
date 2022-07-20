from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models.job import Job

class RootCause(models.Model):
    cause = models.CharField(_("cause"), max_length=144, null=False, blank=True)
    findings = models.TextField(_("findings"), null=True, blank=True)
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="root_cause", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("root cause")
        verbose_name_plural = _("root causes")

    def __str__(self):
        return self.cause

    def get_absolute_url(self):
        return reverse("root_cause_detail", kwargs={"pk": self.pk})
