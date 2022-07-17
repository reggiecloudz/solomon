from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Client

class Questionnaire(models.Model):
    label = models.CharField(_("label"), max_length=144, null=False, blank=True)
    description = models.TextField(_("description"), null=False, blank=True)
    is_complete = models.BooleanField(default=False, null=False, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='questionnaires', blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk":self.pk})

class QuestionnaireItem(models.Model):
    question = models.CharField(_("question"), max_length=144, null=False, blank=True)
    is_answered = models.BooleanField(default=False, null=False, blank=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="items", null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("questionnaire item")
        verbose_name_plural = _("questionnaire items")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("questionnaire_item_detail", kwargs={"pk": self.pk})
