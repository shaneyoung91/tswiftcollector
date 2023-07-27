from django.db import models
from django.urls import reverse

# Create your models here.
class TSwift(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    songs = models.TextField(max_length=250)
    taylors_version = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tswift_id': self.id})