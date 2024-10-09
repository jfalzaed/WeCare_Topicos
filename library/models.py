from django.db import models

# Create your models here.
class Mental_contente(models.Model):
    ESTRES = 'estres'
    DEPRESSION = 'depresion'
    ANSIEDAD = 'ansiedad'

    TOPIC_CHOICES = [
        (ESTRES, 'Estrés'),
        (DEPRESSION, 'Depresión'),
        (ANSIEDAD, 'Ansiedad'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/content/images/')
    url = models.URLField(blank=True)
    topic = models.CharField(
        max_length=10,
        choices=TOPIC_CHOICES,
        default=ESTRES,
    )

    def __str__(self):
        return self.title