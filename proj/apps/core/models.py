from django.conf import settings
from django.db import models
from django.utils.translation import get_language
from django.utils import translation

# class MultiLinguaField(models.Field):
#     SUPPORTED_FIELD_TYPES = [models.CharField, models.TextField]

#     def __inti__(self, verbose_name=None, **kwargs):
#         self.localized_field_model = None
#         for model in MultiLinguaField.SUPPORTED_FIELD_TYPES:
#             if issubclass(self, )
