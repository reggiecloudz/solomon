from email.policy import default
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from incidents.models import Job

class Evaluation(models.Model):
    all_passed = models.BooleanField(_("all passed"), default=False, null=False, blank=True)
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="evaluation", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("evaluation")
        verbose_name_plural = _("evaluations")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("evaluation_detail", kwargs={"pk": self.pk})

class EvaluationTest(models.Model):
    task = models.CharField(_("task"), max_length=144, null=False, blank=True)
    passed = models.BooleanField(default=False, null=False, blank=True)
    results = models.TextField(_("results"), null=True, blank=True)
    evaluation = models.ForeignKey(Evaluation, verbose_name=_("evaluation"), on_delete=models.CASCADE, related_name="tests", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("evaluation test")
        verbose_name_plural = _("evaluation tests")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("evaluation_test_detail", kwargs={"pk": self.pk})
