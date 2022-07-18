from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Job

class ProblemDefinition(models.Model):
    # the circumstances that form the setting
    context = models.TextField(_("context"), null=False, blank=True)
    background = models.TextField(_("background"), null=False, blank=True)
    symptoms = models.TextField(_("symptoms"), null=False, blank=True)
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="problem_definition", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("problem definition")
        verbose_name_plural = _("problem definitions")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("problem_definition_detail", kwargs={"pk": self.pk})
