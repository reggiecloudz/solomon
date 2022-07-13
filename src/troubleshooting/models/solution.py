from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Technician
from incidents.models import Incident

# Create your models here.
class Solution(models.Model):
    title = models.CharField(max_length=144, null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name="solutions", null=False, blank=True)
    incident = models.OneToOneField(Incident, on_delete=models.CASCADE, related_name="solution", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("solution")
        verbose_name_plural = _("solutions")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("solution_detail", kwargs={"pk": self.pk})
