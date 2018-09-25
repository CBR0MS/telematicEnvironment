from django.db import models

# a model for storing the interpetations of the whispers
class Interpretation(models.Model):
    interpreted = models.DateField(auto_now=True)
    text = models.CharField(max_length=200)

# a model for the whispers and their interpretations 
class Whisper(models.Model):
    whispered = models.DateField(auto_now=True)
    og_text = models.CharField(max_length=200)
    interpretations = models.ManyToManyField(Interpretation)
