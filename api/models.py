from django.db import models

# Create your models here.


class Leaf(models.Model):
    hindiName = models.CharField(max_length=100, blank=True, null=True)
    sanskritName = models.CharField(max_length=100, blank=True, null=True)
    englishName = models.CharField(max_length=100)
    latinName = models.CharField(max_length=100)
    shortDescription = models.TextField()
    longDescription = models.TextField()
    medicinalUses = models.TextField()

    def __str__(self):
        return self.name
