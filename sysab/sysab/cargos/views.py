# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from .models import TbCargos
from .serializers import CargosSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework import mixins
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# from django.shortcuts import get_object_or_404


class CargosViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    serializer_class = CargosSerializer
    queryset = TbCargos.objects.all()