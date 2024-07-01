from rest_framework import serializers
from rest_framework import generics
from .models import Doctor, Clinic, DoctorClinic, InsuranceProvider, DoctorInsurance, Appointment, ServiceProvided, Certification, ResearchPublication

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

class DoctorClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorClinic
        fields = '__all__'

class InsuranceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceProvider
        fields = '__all__'

class DoctorInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInsurance
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ServiceProvidedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvided
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class ResearchPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPublication
        fields = '__all__'


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
        clinics = obj.doctorclinic_set.all()  # Access related DoctorClinic objects
        return ClinicSerializer([doctor_clinic.clinic for doctor_clinic in clinics], many=True).data

    def get_insurance_providers(self, obj):
        insurance_providers = obj.doctorinsurance_set.all()  # Access related DoctorInsurance objects
        return InsuranceProviderSerializer([doctor_insurance.insurance_provider for doctor_insurance in insurance_providers], many=True).data

    def get_appointments(self, obj):
        appointments = obj.appointment_set.all()  # Access related Appointment objects
        return AppointmentSerializer(appointments, many=True).data

    def get_services_provided(self, obj):
        services_provided = obj.serviceprovided_set.all()  # Access related ServiceProvided objects
        return ServiceProvidedSerializer(services_provided, many=True).data

    def get_certifications(self, obj):
        certifications = obj.certification_set.all()  # Access related Certification objects
        return CertificationSerializer(certifications, many=True).data

    def get_research_publications(self, obj):
        research_publications = obj.researchpublication_set.all()  # Access related ResearchPublication objects
        return ResearchPublicationSerializer(research_publications, many=True).data