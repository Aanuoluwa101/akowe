from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() 

class Officiator(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    rank = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    can_conduct_on_weekdays = models.BooleanField()
    can_conduct_on_sundays = models.BooleanField()
    can_read_on_weekdays = models.BooleanField()
    can_read_on_sundays = models.BooleanField()
    can_preach_on_weekdays = models.BooleanField()
    can_preach_on_sundays = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    secretary = models.ForeignKey(User, on_delete=models.CASCADE, related_name="officiators")

    def __str__(self) -> str:
        return f"{self.rank} {self.name}"
    

