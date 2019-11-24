from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    start_date = models.DateTimeField('date started')
    def __str__(self):
        return self.service_name