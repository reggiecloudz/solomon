from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from incidents.models import Incident

class Part(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='parts', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("part")
        verbose_name_plural = _("parts")

    def __str__(self):
        return f"{self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("part_detail", kwargs={"pk": self.pk})
