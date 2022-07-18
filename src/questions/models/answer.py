from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Technician
from questions.models import Question

class Answer(models.Model):
    response = models.CharField(_("response"), max_length=255, null=False, blank=True)
    explanation = models.TextField(_("explanation"), null=False, blank=True)
    is_read = models.BooleanField(default=False, null=False, blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="answer", blank=True, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers', blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("answer")
        verbose_name_plural = _("answers")

    def __str__(self):
        return self.response

    def get_absolute_url(self):
        return reverse("answer_detail", kwargs={"pk":self.pk})
