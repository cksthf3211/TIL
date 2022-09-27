from django.db import models

# Create your models here.

class Article(models.Model):
    content = models.TextField() # python manage.py makemigrations
                                 # python manage.py migrate