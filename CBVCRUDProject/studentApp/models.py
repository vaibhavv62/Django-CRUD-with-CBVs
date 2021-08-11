from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField(verbose_name='Roll No')
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    marks = models.FloatField()

    def __str__(self) -> str:
        return f"{self.rn},{self.name}"
