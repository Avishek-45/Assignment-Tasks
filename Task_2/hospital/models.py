from django.db import models
from account.models import User


class Receptionist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptionist')
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    joined_on = models.DateField(auto_now_add=True)


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    specialist = models.CharField(max_length=100, blank=True, null=True)
    joined_on = models.DateField(auto_now_add=True)

class Patient(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    illness = models.CharField(max_length=200, blank=True, null=True)
    symptoms = models.CharField(max_length=300, blank=True, null=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_doctor')
    checked_up = models.DateField(auto_now=True)

# Create your models here.
