from django.db import models

# Create your models here.
class pet(models.Model):
    gender=(("MALE","male"),("FEMALE","female"))
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    price=models.FloatField()
    gender=models.CharField(max_length=200,choices=gender)

    class Meta:
        db_table="pet"