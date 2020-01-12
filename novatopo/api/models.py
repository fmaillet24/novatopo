from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(null=False, max_length=255)
    price = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=255)
    descriptions = models.TextField()
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(null=False, max_length=255)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='business')


class ActivityAvailable(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='activityAvailable')
    date = models.DateTimeField()


class Booking(models.Model):
    name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=255)
    participant = models.IntegerField()
    date = models.DateTimeField()
    total = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='booking', default=1)

    def __str__(self):
        return self.name
