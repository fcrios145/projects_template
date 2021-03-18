from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(default='', max_length=60)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    month = models.ForeignKey('Month', on_delete=models.CASCADE, null=True, blank=True)

class Month(models.Model):
    name = models.CharField(default='', max_length=60)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)

