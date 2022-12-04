from django.db import models


class Tour(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    duration = models.BigIntegerField()
    origin = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    sleeper_fare = models.BigIntegerField(blank=True)
    ac_fare = models.BigIntegerField(blank=True)
    image = models.ImageField(upload_to='home/images')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/images')
