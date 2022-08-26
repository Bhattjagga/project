from django.db import models

# Create your models here.
class MoviesDetails(models.Model):
    title=models.CharField(max_length=300,null=True)
    release_year=models.DateField(null=True)
    genres=models.CharField(max_length=300,null=True)
    director=models.CharField(max_length=250,null=True)
    actor=models.CharField(max_length=250,null =True)
    language=models.CharField(max_length=250,null=True)
    rating=models.FloatField(default=0)

