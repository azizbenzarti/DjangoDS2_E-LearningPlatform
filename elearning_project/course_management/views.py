# course_management/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elearning_app.models import Course,Tutor
from elearning_app.serializers import CourseSerializer,TutorSerializer
from tutor_features.views import get_tutor_id_by_name


#List all
@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

#get by id
@api_view(['GET'])
def get_course_by_id(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course)
    return Response(serializer.data)
"""""
#get course id
@api_view(['GET'])
def get_courses_by_tutor(request, tutor_name):
    courses = Course.objects.filter(tutor__id=get_tutor_id_by_name['tutor_id']) #a tester ??
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
"""

@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
