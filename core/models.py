from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    days = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    payed = models.FloatField()

    def __str__(self):
        return f"{self.user} Reserved {self.start_date} - {self.end_date}: {self.days} days"
