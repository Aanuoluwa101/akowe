from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.comment} - {self.username}"