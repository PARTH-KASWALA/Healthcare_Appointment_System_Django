from django.db import models

# Create your models here.

import uuid
from django.contrib.auth.models import User

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

def __str__(self):
    return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    availability_schedule = models.TextField()

def __str__(self):
        return self.user.get_full_name()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_history = models.TextField(blank=True, null=True)
    
def __str__(self):
        return self.user.get_full_name()


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending')
    # patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    symptoms = models.TextField(blank=True, null=True)
    
def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.last_name} for {self.patient.user.last_name}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, related_name='medical_records', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='medical_records', on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    lab_results = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Record for {self.patient.user.get_full_name()} on {self.record_date.strftime('%Y-%m-%d')}"
    
    
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, related_name='prescription', on_delete=models.CASCADE)
    medication = models.TextField()
    dosage = models.CharField(max_length=255)
    instructions = models.TextField()
    issued_date = models.DateTimeField()

    def __str__(self):
        return f"Prescription for {self.appointment.patient.user.get_full_name()} on {self.issued_date.strftime('%Y-%m-%d')}"
    