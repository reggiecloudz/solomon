from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Implementation

class Phase(models.Model):
    label = models.CharField(_("label"), max_length=144, null=False, blank=True)
    is_complete = models.BooleanField(_("is complete"), default=False, null=False, blank=True)
    implementation = models.ForeignKey(Implementation, on_delete=models.CASCADE, related_name="phases", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("phase")
        verbose_name_plural = _("phases")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("phase_detail", kwargs={"pk": self.pk})
