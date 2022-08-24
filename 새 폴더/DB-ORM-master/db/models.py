import sys
from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

    # create 메서드 활용
    # Genre.objects.create(name = '발라드')

    # 인스턴스 조작
    # genre = genre()
    # genre.name = '인디밴드'
    # genre.save()

# 