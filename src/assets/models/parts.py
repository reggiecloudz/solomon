from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from assets.models import Device, device


class Part(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='parts', null=False, blank=True)
    cost = models.DecimalField(_("cost"), max_digits=5, decimal_places=2, null=True, blank=True)
    # resource, url, title, description
    documentation = models.JSONField(default=list, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("part")
        verbose_name_plural = _("parts")

    def __str__(self):
        return f"{self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("part_detail", kwargs={"pk": self.pk})
