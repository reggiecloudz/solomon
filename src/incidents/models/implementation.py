from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Solution

class Implementation(models.Model):
    plan = models.TextField(_("plan"), null=False, blank=True)
    start_date = models.DateTimeField(_("start date"), null=True, blank=True)
    documentation = models.JSONField(default=list, null=True, blank=True)
    tools = models.JSONField(default=list, null=True, blank=True)
    solution = models.OneToOneField(Solution, on_delete=models.CASCADE, related_name="implementation", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("implementation")
        verbose_name_plural = _("implementations")

    def __str__(self):
        return f"{self.solution.label} implementation"

    def get_absolute_url(self):
        return reverse("implementation_detail", kwargs={"pk": self.pk})
