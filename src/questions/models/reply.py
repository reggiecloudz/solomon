from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Technician
from questions.models import Answer

class Reply(models.Model):
    comment = models.TextField(null=False, blank=True)
    author = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name="replies", null=False, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='replies', null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("reply")
        verbose_name_plural = _("replies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("reply_detail", kwargs={"pk": self.pk})
