from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request, format=None):
        return Response({'msg': 'Registration Success'})
