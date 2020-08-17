from django.db import models
from datetime import time


class Services(models.Model):
    serviceName = models.CharField(max_length=100)
    ServicePrice = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.serviceName},price:{self.ServicePrice} Huf"


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    appointment_date = models.DateField()
    appointment_time = models.TimeField(default=time(11))
    phone_Numebr = models.IntegerField(default=0)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name} at {self.appointment_time} on {self.appointment_date} Phone:{self.phone_Numebr} Service:{self.service}"
