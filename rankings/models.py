from django.db import models

# Create your models here.
class Rank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=50)
    weight = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"