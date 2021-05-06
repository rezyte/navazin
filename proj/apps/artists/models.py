from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(
        max_length=225, 
        blank=True,
        null=True,
        verbose_name= _("نام هنرمند")
    )
    last_name = models.CharField(
        max_length=225, 
        blank=True,
        null=True,
        verbose_name= _("نام خانوادگی هنرمند")
    )
    alias = models.CharField(
        max_length=225, 
        verbose_name= _("نام")
    )

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name_plural = _("هنرمندان")
        