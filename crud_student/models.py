from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return "%s" %(self.name)