from django.db import models

# Create your models here.
class Project(models.Model):
    img = models.ImageField(default='default.png', blank=True)
    url_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.url_name
