from django.db import models

from measurements.models import Measurement

class Alarm(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    variables = models.ManyToManyField(Measurement)
    
    def __str__(self):
        return '%s %s' % (self.name, self.time)
