from django.db import models

# Create your models here.
# class PostModel(models.Model):
    # title = models.CharField(max_length = 200)
    # description = models.TextField()
class Details(models.Model):
    name = models.CharField(max_length= 200)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        # return self.title
        return self.name