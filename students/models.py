from django.db import models

class Student(models.Model):
    id_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name

