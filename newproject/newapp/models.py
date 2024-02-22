from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title = models.CharField(max_length=40)
    desc= models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallary')

    

