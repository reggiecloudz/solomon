from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from troubleshooting.models import Solution

class Step(models.Model):
    label = models.CharField(max_length=144, null=False, blank=True)
    step_number = models.PositiveSmallIntegerField(null=False, blank=True)
    is_complete = models.BooleanField(default=False, null=False, blank=True)
    # [{'findings', 'reference', 'action', 'outcome'}]
    # Step.objects.filter(documentation__contains=[{'reference': 'https://example.com'}])
    documentation = models.JSONField(null=True, blank=True)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='steps', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("step")
        verbose_name_plural = _("steps")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("step_detail", kwargs={"pk": self.pk})
