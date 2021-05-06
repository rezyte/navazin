from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth import get_user_model

user = get_user_model()

class Rating(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    object_id = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE,
        limit_choices_to={
            "model_in": ["songs", "artists"]
        }
    )
    content_object = GenericRelation