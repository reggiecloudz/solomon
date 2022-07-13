from django.db import models
from django.utils.translation import gettext as _

from assets.models.device import Device

class SystemDescription(models.Model):
    # [{type, brand, in_use, changed_date}]
    device = models.OneToOneField(Device, on_delete=models.CASCADE, related_name='system_descriptions', null=False, blank=True)
    architecture = models.CharField(max_length=20, null=True, blank=True)
    display_type = models.JSONField(null=True, blank=True)
    operating_system = models.JSONField(null=False, blank=True)
    processor_type = models.CharField(max_length=144, null=True, blank=True)
    number_of_processors = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    pci_slots = models.JSONField(null=True, blank=True)
    # [{type, brand, position, in_use, changed_date}]
    hard_drives = models.JSONField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("system_description")
        verbose_name_plural = _("system_descriptions")
