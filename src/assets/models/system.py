from email.policy import default
from django.db import models
from django.forms import JSONField
from django.utils.translation import gettext as _

from assets.models import Device

class SystemSnapshot(models.Model):
    # [{type, brand, in_use, changed_date}]
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='system_snapshots', null=False, blank=True)
    display_type = models.JSONField(default=list, null=True, blank=True)
    operating_system = models.JSONField(default=list, null=False, blank=True)
    processor_type = models.CharField(max_length=144, null=True, blank=True)
    number_of_processors = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    pci_slots = models.JSONField(default=list, null=True, blank=True)
    # [{type, brand, position, in_use, changed_date}]
    hard_drives = models.JSONField(default=list, null=True, blank=True)
    # resource, url, title, description
    documentation = models.JSONField(default=list, null=True, blank=True)
    benchmarks = models.JSONField(default=dict, null=True, blank=True)
    changes = models.JSONField(default=list, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("system description")
        verbose_name_plural = _("system descriptions")

    def __str__(self):
        return self.device.brand
