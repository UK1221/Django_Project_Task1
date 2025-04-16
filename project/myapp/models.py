from django.db import models

# Create your models here.
class Post(models.Model):
    animalphoto=models.ImageField(upload_to='profiles/')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def str(self):
        return self.title