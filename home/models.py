from django.db import models

class notes(models.Model):
    name=models.CharField(max_length=250,default=True)
    img=models.ImageField(upload_to="image")
    desc=models.TextField()

