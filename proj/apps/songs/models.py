from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=225)
    lyrics = RichTextField()
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    voice = models.FileField()

    

