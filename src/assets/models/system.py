from email.policy import default
from django.db import models
from django.forms import JSONField
from django.utils.translation import gettext as _

from assets.models import Device

class SystemSnapshot(models.Model):
    # [{type, brand, in_use, changed_date}]
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='system_snapshots', null=False, blank=True)
    case = models.CharField(_("case"), max_length=144, null=True, blank=True)
    motherboard = models.CharField(_("motherboard"), max_length=144, null=True, blank=True)
    bios = models.JSONField(default=dict, null=True, blank=True)
    visual_display_unit = models.JSONField(_("visual display unit"), default=dict, null=True, blank=True)
    operating_system = models.CharField(_("operating system"), max_length=144, null=False, blank=True)
    architecture = models.CharField(max_length=144, null=True, blank=True)
    processor = models.JSONField(default=dict, null=True, blank=True)
    graphics_card = models.JSONField(_("graphics card"), default=dict, null=True, blank=True)
    sound_card = models.JSONField(_("sound card"), default=dict, null=True, blank=True)
    ram = models.JSONField(default=dict, null=True, blank=True)
    pci_slots = models.JSONField(_("pci slots"), default=list, null=True, blank=True)
    hard_drives = models.JSONField(default=list, null=True, blank=True)
    cooling = models.JSONField(default=dict, null=True, blank=True)
    power_supply = models.JSONField(_("power supply"), default=dict, null=True, blank=True)
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
