from django.db import models

class USERS(models.Model):
    name = models.CharField(max_length=30)
    u_id = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    credits = models.IntegerField()
    balance = models.IntegerField()
    contact = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)

class TRIP(models.Model):
    trip_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=20)
    destn = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    u_id = models.ForeignKey(USERS)



class TASK(models.Model):
    task_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=20)
    destn = models.CharField(max_length=20)
    budget = models.IntegerField()
    u_id = models.ForeignKey(USERS)


class TASK_STATUS(models.Model):
    trip_id = models.ForeignKey(TRIP)
    task_id = models.ForeignKey(TASK)
    status_id = models.IntegerField()

class TRIP_STATUS(models.Model):
    trip_id = models.ForeignKey(TRIP)
    task_id = models.ForeignKey(TASK)
    status_id = models.IntegerField()