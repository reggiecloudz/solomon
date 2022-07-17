from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models.job import Job

class Implementation(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="job", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("implementation")
        verbose_name_plural = _("implementations")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("implementation_detail", kwargs={"pk": self.pk})
