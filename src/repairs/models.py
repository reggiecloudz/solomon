from re import I
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from .choices import REPAIR_STATUS_CHOICES
from accounts.models import Client, Technician

class Device(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    operating_system = models.CharField(max_length=64, null=False, blank=True)
    about = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devices', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("device")
        verbose_name_plural = _("devices")

    def __str__(self):
        return f"{self.client.identity.name}'s {self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("device_detail", kwargs={"pk": self.pk})

class Repair(models.Model):
    subject = models.CharField(max_length=144, null=False, blank=True)
    explanation = models.TextField(null=False, blank=True)
    status = models.CharField(max_length=60, default="Submitted", choices=REPAIR_STATUS_CHOICES, null=False, blank=True)
    start_date = models.DateField(null=True, blank=True)
    resolved_date = models.DateField(null=True, blank=True)
    start_work_time = models.TimeField(null=True, blank=True)
    end_work_time = models.TimeField(null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="repairs", null=False, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="repairs", null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, related_name="repairs", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("repair")
        verbose_name_plural = _("repairs")

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("repair_detail", kwargs={"pk": self.pk})


class Part(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=True)
    model = models.CharField(max_length=100, null=False, blank=True)
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, related_name='repairs', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("part")
        verbose_name_plural = _("parts")

    def __str__(self):
        return f"{self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("part_detail", kwargs={"pk": self.pk})

class Solution(models.Model):
    title = models.CharField(max_length=144, null=False, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name="solutions", null=False, blank=True)
    repair = models.OneToOneField(Repair, on_delete=models.CASCADE, related_name="solution", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("solution")
        verbose_name_plural = _("solutions")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("solution_detail", kwargs={"pk": self.pk})

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
