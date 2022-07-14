from django.urls import include, path
from .views import *

urlpatterns = [
    path('receptionist/', ReceptionistAPIView.as_view(), name='receptioonist'),
    path('doctor/', DoctorAPIView.as_view(), name='doctor'),
    path('patient/', PatientAPIView.as_view(), name='patient'),
    path('patient/<int:id>/', PatientRudView.as_view(), name='patientrud'),
    path('login/', LoginView.as_view(), name='login'),
]