from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import (
#     DoctorViewSet, 
#     PatientViewSet, 
#     AppointmentViewSet, 
#     MedicalRecordViewSet, 
#     PrescriptionViewSet, 
#     SpecializationViewSet
# )



# router = DefaultRouter()
# router.register(r'doctors', DoctorViewSet)
# router.register(r'patients', PatientViewSet)
# router.register(r'appointments', AppointmentViewSet)
# router.register(r'medical_records', MedicalRecordViewSet)
# router.register(r'prescriptions', PrescriptionViewSet)
# router.register(r'specializations', SpecializationViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
# ]

# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Doctor URLs
    path('doctors/', views.doctor_list, name='doctor-list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor-detail'),

    # Patient URLs
    path('patients/', views.patient_list, name='patient-list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient-detail'),

    # Appointment URLs
    path('appointments/', views.appointment_list, name='appointment-list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment-detail'),

    # Medical Record URLs
    path('medical_records/', views.medical_record_list, name='medical-record-list'),
    path('medical_records/<int:pk>/', views.medical_record_detail, name='medical-record-detail'),

    # Prescription URLs
    path('prescriptions/', views.prescription_list, name='prescription-list'),
    path('prescriptions/<int:pk>/', views.prescription_detail, name='prescription-detail'),

    # Specialization URLs
    path('specializations/', views.specialization_list, name='specialization-list'),
    path('specializations/<int:pk>/', views.specialization_detail, name='specialization-detail'),
]
