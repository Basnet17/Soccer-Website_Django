from django.db import models

# Create your models here.
class playersInfo(models.Model):
    Name = models.CharField(max_length=120, )
    description = models.TextField()
    Club = models.TextField()
    Strength = models.TextField(default='Filled with Skill!')
    summary = models.TextField(default= 'This is cool!')
    picture = models.ImageField(upload_to='',max_length=100, default="default.jpg",blank=True )

class predictions(models.Model):
    name = models.CharField(max_length = 100,)
    def enterName():
        return "Your Name is"
