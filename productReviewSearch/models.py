from django.db import models


# Create your models here.

class Product(models.Model):
    productId = models.CharField(max_length=20, primary_key=True)
    userId = models.CharField(max_length=20)
    profileName = models.CharField(max_length=20)
    helpfulness = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=10, decimal_places=1)
    time = models.TimeField()
    summary = models.CharField(max_length=60)
    reviewText = models.CharField(max_length=500)

    def __str__(self):
        return f' {self.reviewText} {self.score} {self.helpfulness}'
