import email
from rest_framework.response import Response
from rest_framework import (
    generics, 
    permissions, 
    status, 
    )
from rest_framework.views import APIView
from .models import Receptionist, Patient, Doctor
from .serializers import UserSerializer, DoctorSerializer, PatientSerializer, ReceptionistSerializer
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permissions_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReceptionistAPIView(generics.ListCreateAPIView):
    serializer_class = ReceptionistSerializer
    permissions_classes = (permissions.AllowAny,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Receptionist.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = request.data
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(email=data.get('email'))
        user.set_password(data.get('password'))
        user.staff = True
        user.save()
        serializer.save(user=user)
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DoctorAPIView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permissions_classes = (permissions.AllowAny,)

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.staff == True:
            return Doctor.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = request.data
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(email=data.get('email'))
        user.set_password(data.get('password'))
        user.doctor = True
        user.save()
        serializer.save(user=user)
        refresh = RefreshToken.for_user(user)
        print("refresh", refresh)
        token = str(refresh.access_token)
        print("access", token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PatientAPIView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permissions_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.staff == True:
            return Patient.objects.all()
        else:
            return Patient.objects.filter(assigned_doctor=self.request.user)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PatientRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        if self.request.user.staff == True:
            id = self.kwargs['id']
            data = self.request.data
            if Patient.objects.filter(id=id).exists():
                patient = Patient.objects.get(id=id)
                if data.get('name') is not None:
                    patient.name=data.get('name')
                if data.get('address') is not None:
                    patient.address=data.get('address')
                if data.get('phone') is not None:
                    patient.phone=data.get('phone')
                if data.get('illness') is not None:
                    patient.illness=data.get('illness')
                if data.get('symptoms') is not None:
                    patient.symptoms=data.get('symptoms')
                if data.get('assigned_doctor') is not None:
                    if Doctor.objects.filter(id=data.get('assigned_doctor')).exists():
                        patient.assigned_doctor=Doctor.objects.get(id=data.get('assigned_doctor'))
                patient.save()
        else:
            return Response({"message":"You are not Receptionist"}, status=401)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = User.objects.get(email=email.lower())
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Wrong password!')

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'userfield': email,
            'token': token,
        }
        return response



