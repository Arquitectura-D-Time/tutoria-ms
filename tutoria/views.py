from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tutoria
from .serializers import TutoriaS

# Create your views here.

@api_view(['GET', 'POST'])
def TutoriaList(request):
   
    if request.method == 'GET':
        snippets = Tutoria.objects.all()
        serializer = TutoriaS(snippets, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TutoriaS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)