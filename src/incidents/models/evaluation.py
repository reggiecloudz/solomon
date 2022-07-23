from email.policy import default
from django.db import models
from django.forms import JSONField
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Job

class Evaluation(models.Model):
    all_passed = models.BooleanField(_("all passed"), default=False, null=False, blank=True)
    tests = models.JSONField(default=list, null=True, blank=True)
    # [{label, passed, results}]
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="evaluation", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("evaluation")
        verbose_name_plural = _("evaluations")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("evaluation_detail", kwargs={"pk": self.pk})
