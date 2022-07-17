from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from assets.models import Device

class Update(models.Model):
    publisher = models.CharField(_("publisher"), max_length=75, null=False, blank=True)
    name = models.CharField(_("name"), max_length=144, null=False, blank=True)
    version = models.CharField(_("version"), max_length=75, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    # resource, url, title, description
    documentation = models.JSONField(default=list, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='updates', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("update")
        verbose_name_plural = _("updates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("update_detail", kwargs={"pk": self.pk})
