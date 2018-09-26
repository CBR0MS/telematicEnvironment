from django.db import models
import uuid

# a model for storing the interpetations of the whispers
class Interpretation(models.Model):
    interpreted = models.DateField(auto_now=True)
    text = models.CharField(max_length=200)

# a model for the whispers and their interpretations 
class Whisper(models.Model):
    id = models.CharField(primary_key=True, max_length=100, blank=True, unique=True, default=uuid.uuid4)
    whispered = models.DateField(auto_now=True)
    og_text = models.CharField(max_length=200)
    display_text = models.CharField(max_length=200, blank=True)
    interpretations = models.ManyToManyField(Interpretation, blank=True)
