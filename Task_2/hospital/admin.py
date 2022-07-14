from django.contrib import admin
from .models import Receptionist, Doctor, Patient

admin.site.register(Receptionist)
admin.site.register(Doctor)
admin.site.register(Patient)

# Register your models here.
