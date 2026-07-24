from django.db import models

# Create your models here.
class td_model(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title