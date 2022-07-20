from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Notication(models.Model):
    label = models.CharField(_("label"), max_length=100, null=False, blank=True)
    text = models.TextField(_("text"), null=False, blank=True)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications", null=False, blank=True)
    url = models.CharField(_("url"), max_length=144, null=True, blank=True)
    button_text = models.CharField(_("button text"), max_length=20, null=False, blank=True)
    is_read = models.BooleanField(_("is read"), default=False, null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("notication")
        verbose_name_plural = _("notications")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("notication_detail", kwargs={"pk": self.pk})
