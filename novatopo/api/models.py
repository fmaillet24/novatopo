from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name


class BusinessActivity(models.Model):
    name = models.CharField(null=False, max_length=255)
    price = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=255)
    descriptions = models.TextField()
    is_staff = models.BooleanField(default=False)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='activities')
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='businesses')

    def __str__(self):
        return self.name


class ActivityAvailable(models.Model):
    date = models.DateTimeField()
    activity = models.ForeignKey(
        BusinessActivity, on_delete=models.CASCADE, related_name='activityAvailable')


class Booking(models.Model):
    name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=255)
    participant = models.IntegerField()
    date = models.DateTimeField()
    total = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activity = models.ForeignKey(
        BusinessActivity, on_delete=models.CASCADE, related_name='booking', default=1)

    def __str__(self):
        return self.name
