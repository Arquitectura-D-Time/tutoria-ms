from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tutoria
from .serializers import TutoriaS

# Create your views here.

@api_view(['GET', 'POST','DELETE'])
def BasicTutoria(request):
   
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
    if request.method=='DELETE':
        Tutoria.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def AdvanceTutoria(request, pk):
    try:
        snippet = Tutoria.objects.get(pk=pk)
    except Tutoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TutoriaS(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TutoriaS(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def SearchTutoria(request, materia):
    try:
        snippet = Tutoria.objects.filter(materia=materia)
    except Tutoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TutoriaS(snippet,many=True)
        return Response(serializer.data)