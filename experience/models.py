from django.db import models

# Create your models here.
class Activity(models.Model):
    work_place = models.CharField(max_length=100)
    description = models.TextField()
    period_from = models.DateField()
    period_to = models.DateField()

    def __str__(self):
        return self.work_place
