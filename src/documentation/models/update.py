from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from assets.models.device import Device

class Update(models.Model):
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
