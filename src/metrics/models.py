from email.policy import default
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import JSONField
from django.urls import reverse
from django.utils.translation import gettext as _

PRECENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Statistic(models.Model):
    label = models.CharField(_("label"), max_length=75, null=False, blank=True)
    dataset = JSONField(default=list, null=True, blank=True)

    class Meta:
        verbose_name = _("statistic")
        verbose_name_plural = _("statistics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("statistic_detail", kwargs={"pk": self.pk})
    
    def get_mean(self):
        # The mean (average) of a data set is found by adding all numbers in the data set and then dividing by the number of values in the set
        pass

    def get_median(self):
        # The median is the middle value when a data set is ordered from least to greatest.
        pass
    
    def get_mode(self):
        # The mode is the number that occurs most often in a data set.
        pass
