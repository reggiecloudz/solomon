from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Question(models.Model):
    inquiry = models.CharField(_("inquiry"), max_length=255, null=False, blank=True)
    content = models.TextField(_("content"), null=False, blank=True)
    is_answered = models.BooleanField(default=False, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions', blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.inquiry

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk":self.pk})
