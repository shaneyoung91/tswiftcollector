from django.db import models

# Create your models here.
class TSwift(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    songs = models.TextField(max_length=250)
    taylors_version = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.name}'