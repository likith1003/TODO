from django.db import models

# Create your models here.
class todo(models.Model):
    sno=models.IntegerField(("Sno"),primary_key=True)
    title=models.CharField(("Title"), max_length=50)
    desc=models.TextField(("Desc"))