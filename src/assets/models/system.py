from django.db import models
from django.utils.translation import gettext as _

from assets.models import Device

class SystemDescription(models.Model):
    # [{type, brand, in_use, changed_date}]
    device = models.OneToOneField(Device, on_delete=models.CASCADE, related_name='system_descriptions', null=False, blank=True)
    architecture = models.CharField(max_length=20, null=True, blank=True)
    display_type = models.JSONField(default=list, null=True, blank=True)
    operating_system = models.JSONField(default=list, null=False, blank=True)
    processor_type = models.CharField(max_length=144, null=True, blank=True)
    number_of_processors = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    pci_slots = models.JSONField(default=list, null=True, blank=True)
    # [{type, brand, position, in_use, changed_date}]
    hard_drives = models.JSONField(default=list, null=True, blank=True)
    # resource, url, title, description
    documentation = models.JSONField(default=list, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("system description")
        verbose_name_plural = _("system descriptions")

    def __str__(self):
        return self.device.brand
