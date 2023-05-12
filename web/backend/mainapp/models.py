from django.db import models

# Create your models here.

class Result(models.Model):
    result = models.CharField(max_length=500)

    def __str__(self) -> str:
        return super().__str__()