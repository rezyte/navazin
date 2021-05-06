from django.db import models
from django.db.models import Q

from ckeditor.fields import RichTextField

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=225)
    lyrics = RichTextField()
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    voice = models.FileField()
    
    @staticmethod
    def average_rating(self):
        from proj.apps.ratings.models import Rating
        q = Q(content_object__id__iexact=self.id)
        ratings = Rating.objects.filter(q)
        # avg = 
        return None

