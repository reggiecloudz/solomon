from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from assets.models import SystemSnapshot

class Software(models.Model):
    publisher = models.CharField(_("publisher"), max_length=75, null=False, blank=True)
    name = models.CharField(_("name"), max_length=144, null=False, blank=True)
    version = models.CharField(_("version"), max_length=75, null=False, blank=True)
    type = models.CharField(_("type"), max_length=50, null=False, blank=True)
    license_key = models.CharField(_("license key"), max_length=144, null=True, blank=True)
    location = models.CharField(_("location"), max_length=144, null=False, blank=True)
    snapshot = models.ForeignKey(SystemSnapshot, on_delete=models.CASCADE, related_name="software", null=False, blank=True)
    cost = models.DecimalField(_("cost"), max_digits=5, decimal_places=2, null=True, blank=True)
    is_installed = models.BooleanField(null=False, blank=True)
    # resource, url, title, description
    documentation = models.JSONField(default=list, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("software")
        verbose_name_plural = _("software")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("software_detail", kwargs={"pk": self.pk})
