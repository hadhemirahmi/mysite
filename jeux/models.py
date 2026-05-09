from django.db import models

# Create your models here.
class Jeu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='jeux_images/', blank=True, null=True)

    def __str__(self):
        return self.name
        