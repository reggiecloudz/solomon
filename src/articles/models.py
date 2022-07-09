import uuid
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext as _

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("title"), max_length=255, null=False, blank=True)
    video_url = models.URLField(_("video url"), max_length=255, null=True, blank=True)
    content = models.TextField(_("content"), null=False, blank=True)
    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles', editable=False, blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk":self.pk,"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
class Comment(models.Model):
    content = models.TextField(_("content"), null=False, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', editable=False, blank=True, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', editable=False, blank=True, null=False)
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="children", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return f"{self.author.email} commented on {self.article.title} at {self.created}"

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes', editable=False, blank=True, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', editable=False, blank=True, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("like")
        verbose_name_plural = _("likes")

    def __str__(self):
        return f"{self.user.email} likes {self.article.title}"

    def get_absolute_url(self):
        return reverse("like_detail", kwargs={"user_id": self.user.pk, "article_id": self.article.pk})
