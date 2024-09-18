from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets,serializers,response
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor, Patient, Appointment, Prescription, MedicalRecord,Specialization
from .serializers import (
    SpecializationSerializer,
    DoctorSerializer,
    PatientSerializer,
    AppointmentSerializer,
    MedicalRecordSerializer,
    PrescriptionSerializer,
)


#---------------------specialization------------------

@api_view(['GET','POST'])
def specialization_list(request):
    if request.method == 'GET':
        specializations = Specialization.objects.all()
        serializers = SpecializationSerializer(specializations, many=True)
        return response(serializers.data)
    elif request.method == 'POST':
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
def specialization_detail(request,pk):
    try:
        specialization = Specialization.objects.get(pk=pk)
    except Specialization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SpecializationSerializer(specialization,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#---------------------------Doctor -------------------------

@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializers = DoctorSerializer(doctors, many=True)
        return response(serializers.data)
    elif request.method == 'POST':
        serializer = DoctorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer



#----------------Patient---------------------------

@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializers = PatientSerializer(patient, many=True)
        return response(serializers.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer




# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

@api_view(["GET", "POST"])
def appointment_list(request):
    if request.method == "GET":
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except:
        Appointment.DoesNotExist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["GET","POST"])
def medical_record_list(request):
    if request.method == "GET":
        medical_records = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def medical_record_detail(request, pk):
    try:
        medical_record = MedicalRecord.objects.get(pk=pk)
    except MedicalRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MedicalRecordSerializer(medical_record)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MedicalRecordSerializer(medical_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        medical_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class MedicalRecordViewSet(viewsets.ModelViewSet):
#     queryset = MedicalRecord.objects.all()
#     serializer_class = MedicalRecordSerializer

# class PrescriptionViewSet(viewsets.ModelViewSet):
#     queryset = Prescription.objects.all()
#     serializer_class = PrescriptionSerializer


@api_view(["GET", "POST"])
def prescription_list(request):
    if request.method == "GET":
        prescriptions = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def prescription_detail(request, pk):
    try:
        prescription = Prescription.objects.get(pk=pk)
    except Prescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def specialization_list(request):
    if request.method == "GET":
        specializations = Specialization.objects.all()
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def specialization_detail(request, pk):
    try:
        specialization = Specialization.objects.get(pk=pk)
    except Specialization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SpecializationSerializer(specialization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)