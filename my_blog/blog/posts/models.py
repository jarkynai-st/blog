from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.description

