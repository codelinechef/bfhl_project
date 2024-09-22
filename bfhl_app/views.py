from django.shortcuts import render

# Create your views here.
# bfhl_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BFHLSerializer
import random

class BFHLView(APIView):
    def get(self, request):
        # GET request: Return operation_code
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)

    def post(self, request):
        # POST request: Process the data
        serializer = BFHLSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
