from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    job1=models.CharField(max_length=30)
    salary=models.IntegerField()
    job2=models.CharField(max_length=30)
    salary2=models.IntegerField()
    def __str__(self):
        return self.name;
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})

