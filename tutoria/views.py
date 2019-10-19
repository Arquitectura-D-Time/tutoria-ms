from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tutoria
from .serializers import TutoriaS

# Create your views here.

class TutoriaList(APIView):

    def get(self,request):
        tutos=Tutoria.objects.all()
        seria=TutoriaS(tutos,many=True)
        return Response(seria.data)
        
    def post(self):
        pass