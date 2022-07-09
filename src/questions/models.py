from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Client, Technician

class Question(models.Model):
    inquiry = models.CharField(_("inquiry"), max_length=255, null=False, blank=True)
    content = models.TextField(_("content"), null=False, blank=True)
    is_answered = models.BooleanField(default=False, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='questions', blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.inquiry

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk":self.pk})

class Answer(models.Model):
    response = models.CharField(_("response"), max_length=255, null=False, blank=True)
    explanation = models.TextField(_("explanation"), null=False, blank=True)
    is_read = models.BooleanField(default=False, blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="answer", blank=True, null=False)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name='answers', blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("answer")
        verbose_name_plural = _("answers")

    def __str__(self):
        return self.response

    def get_absolute_url(self):
        return reverse("answer_detail", kwargs={"pk":self.pk})

class Reply(models.Model):
    comment = models.TextField(null=False, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="replies", null=False, blank=True)
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
