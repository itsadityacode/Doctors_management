"""
URL configuration for doctor_directory_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from doctor import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    # path('api/', include('doctor_directory_api.urls')),
    path('doctors/details/<int:pk>/', views.DoctorDetailsAPIView.as_view(), name='doctor-details'),
    path('doctors/', views.DoctorListCreate.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroy.as_view(), name='doctor-retrieve-update-destroy'),
    path('clinics/', views.ClinicListCreate.as_view(), name='clinic-list-create'),
    path('clinics/<int:pk>/', views.ClinicRetrieveUpdateDestroy.as_view(), name='clinic-retrieve-update-destroy'),
]
