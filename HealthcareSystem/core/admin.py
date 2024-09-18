from django.contrib import admin

# Register your models here.
from .models import Specialization,Doctor,Patient,Appointment,MedicalRecord,Prescription


admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Prescription)