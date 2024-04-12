from django.db import models

# Create your models here.
class Task(models.Model):
    tittle= models.CharField(max_length=200)
    description= models.TextField(blank=True)
    donde= models.BooleanField(default=False)
    
    # def __self__(self):
    #     return self.tiitle