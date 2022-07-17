from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Technician
from incidents.models import Solution

class Action(models.Model):
    label = models.CharField(_("label"), max_length=144, null=False, blank=True)
    is_complete = models.BooleanField(default=False, null=False, blank=True)
    is_milestone = models.BooleanField(default=False, null=False, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name="actions", null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, related_name="actions", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("action")
        verbose_name_plural = _("actions")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("action_detail", kwargs={"pk": self.pk})
