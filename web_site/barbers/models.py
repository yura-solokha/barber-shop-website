from asyncio.windows_events import NULL
from django.db import models
from django.forms import CharField


class AvailableTime(models.Model):
    time = models.DateTimeField()
    validity = models.BooleanField(default=False)

class Barbers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    available_time = models.ForeignKey(AvailableTime,default=1, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Майстер'
        verbose_name_plural = 'Майстри'

