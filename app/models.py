from django.db import models

# Create your models here.
class Company(models.Model):
    Co_code=models.CharField(max_length=200)
    Co_name=models.CharField(max_length=200)
    IBR_name=models.CharField(max_length=200)
    Face_value=models.FloatField()
    DATE_OF_INCO=models.CharField(max_length=200)
    CNVTOPUBDT=models.CharField(max_length=200)
    def __str__(self):
        return self.Co_code
