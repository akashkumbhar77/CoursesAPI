from django.db import models

# Create your models here.

class CoursesModel(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    isPaid = models.BooleanField()
    price = models.IntegerField()
    numSubscribers = models.IntegerField()
    numReveiws = models.IntegerField()
    numPublishedLectures = models.IntegerField()
    instructionalLevel = models.CharField(max_length=200)
    contentInfo = models.CharField(max_length=200)
    publishedTime = models.CharField(max_length=300)

    def __str__(self):
        return self.title



class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_owner = models.CharField(max_length=200)
    prod_price = models.IntegerField()
    prod_source = models.CharField(max_length=100)

    def __str__(self):
        return self.prod_name