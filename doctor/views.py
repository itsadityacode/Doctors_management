from rest_framework import generics
from django.shortcuts import render
from rest_framework import serializers
from .models import Doctor, Clinic, DoctorClinic, InsuranceProvider, DoctorInsurance, Appointment, ServiceProvided, Certification, ResearchPublication
from .serializers import DoctorSerializer,DoctorDetailsSerializer, ClinicSerializer, DoctorClinicSerializer, InsuranceProviderSerializer, DoctorInsuranceSerializer, AppointmentSerializer, ServiceProvidedSerializer, CertificationSerializer, ResearchPublicationSerializer



class DoctorDetailsAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailsSerializer

class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ClinicListCreate(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    
class DoctorDetailsSerializer(serializers.ModelSerializer):
    clinics = serializers.SerializerMethodField()
    insurance_providers = serializers.SerializerMethodField()
    appointments = serializers.SerializerMethodField()
    services_provided = serializers.SerializerMethodField()
    certifications = serializers.SerializerMethodField()
    research_publications = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = '__all__'

    def get_clinics(self, obj):
        clinics = obj.clinics.all()
        return ClinicSerializer(clinics, many=True).data

    def get_insurance_providers(self, obj):
        insurance_providers = obj.insurance_providers.all()
        return InsuranceProviderSerializer(insurance_providers, many=True).data

    def get_appointments(self, obj):
        appointments = obj.appointments.all()
        return AppointmentSerializer(appointments, many=True).data

    def get_services_provided(self, obj):
        services_provided = obj.services_provided.all()
        return ServiceProvidedSerializer(services_provided, many=True).data

    def get_certifications(self, obj):
        certifications = obj.certifications.all()
        return CertificationSerializer(certifications, many=True).data

    def get_research_publications(self, obj):
        research_publications = obj.research_publications.all()
        return ResearchPublicationSerializer(research_publications, many=True).data


