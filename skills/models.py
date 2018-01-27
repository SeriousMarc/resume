from django.db import models

class Skill(models.Model):
    thumb = models.ImageField(default='default.png', blank=True)
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.title
