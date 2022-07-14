from dataclasses import fields
from pyexpat import model
from unicodedata import name
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Doctor, Patient, Receptionist
from account.models import User

def phonenumber_validation(value):
    if '+977' in value or len(value)>14 or '9' in value:
        pass
    else:
        raise serializers.ValidationError('Invalid Phonenumber')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',]

class ReceptionistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=14, validators=[phonenumber_validation])
    class Meta:
        model = Receptionist
        fields = ['name','address','phone','joined_on']

class DoctorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    contact = serializers.CharField(max_length=14, validators=[phonenumber_validation])
    specialist = serializers.CharField(max_length=200)
    class Meta:
        model = Doctor
        fields = ['name','address','contact','specialist','joined_on']
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'