from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Technician
from incidents.models import Phase

PRECENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Action(models.Model):
    task = models.CharField(_("task"), max_length=144, null=False, blank=True)
    is_complete = models.BooleanField(default=False, null=False, blank=True)
    is_milestone = models.BooleanField(default=False, null=False, blank=True)
    progress = models.DecimalField(_("progress"), max_digits=3, decimal_places=2, default=0.0, validators=PRECENTAGE_VALIDATOR, null=False, blank=True)
    documentation = models.JSONField(default=list, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name="actions", null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, related_name="actions", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("action")
        verbose_name_plural = _("actions")

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("action_detail", kwargs={"pk": self.pk})
