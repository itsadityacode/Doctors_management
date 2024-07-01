from django.contrib import admin
from .models import Doctor, Clinic, DoctorClinic, InsuranceProvider, DoctorInsurance, Appointment, ServiceProvided, Certification, ResearchPublication
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Clinic)
admin.site.register(DoctorClinic)
admin.site.register(InsuranceProvider)
admin.site.register(DoctorInsurance)
admin.site.register(ServiceProvided)
admin.site.register(Certification)
admin.site.register(ResearchPublication)




