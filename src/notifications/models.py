from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Notication(models.Model):
    # label
    # text
    # user
    # url
    # button_text
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("notication")
        verbose_name_plural = _("notications")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("notication_detail", kwargs={"pk": self.pk})
