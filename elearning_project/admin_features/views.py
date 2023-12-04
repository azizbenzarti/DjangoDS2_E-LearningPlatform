from django.shortcuts import render
from rest_framework.decorators import api_view
from elearning_app.models import Tutor
from rest_framework import status
from elearning_app.serializers import TutorSerializer
from rest_framework.response import Response



@api_view(['GET'])
def get_tutor_by_name(request, name):
    try:
        tutor = Tutor.objects.get(username__iexact=name)  # Case-insensitive match    
        serializer = TutorSerializer(tutor)
        return Response({'tutor': serializer.data})
    except Tutor.DoesNotExist:
        return Response({'error': f'Tutor with name {name} not found'}, status=status.HTTP_404_NOT_FOUND)
