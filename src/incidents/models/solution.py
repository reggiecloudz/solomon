from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Job

class Solution(models.Model):
    label = models.CharField(_("label"), max_length=144, null=False, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)
    is_selected = models.BooleanField(_("is selected"), default=False, null=False, blank=True)
    overall_cost = models.DecimalField(_("hourly rate"), max_digits=8, decimal_places=2, default=0.0, null=False, blank=True)
    documentation = models.JSONField(default=list, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="solutions", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("solution")
        verbose_name_plural = _("solutions")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("solution_detail", kwargs={"pk": self.pk})
