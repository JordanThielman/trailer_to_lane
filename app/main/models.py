from django.db import models

# Create your models here.
class Trailer(models.Model):
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.origin

class Package(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    destination_lane = models.IntegerField()
    size = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.destination_lane} - {self.size}"

