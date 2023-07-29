from django.db import models
from django.urls import reverse

# Create your models here.
class Award(models.Model):
    category = models.CharField(max_length=100)
    result = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.tswift.name} - {self.category} - {self.result}'

class TSwift(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    songs = models.TextField(max_length=250)
    taylors_version = models.BooleanField(default=False)
    awards = models.ManyToManyField(Award)
    
    def __str__(self):
        return f'({self.id}) {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tswift_id': self.id})

class DatingHistory(models.Model):
    partner_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    tswift = models.ForeignKey(TSwift, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.tswift.name} - {self.partner_name}'
    