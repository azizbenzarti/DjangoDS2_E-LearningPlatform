
from rest_framework.response import Response
from rest_framework import status
from elearning_app.serializers import StudentSerializer, TutorSerializer,CourseSerializer
from elearning_app.models import Tutor,Course,Student
from rest_framework.decorators import api_view
from django.shortcuts import render,redirect

@api_view(['POST'])
def create_course(request):
    try:
        tutor = Tutor.objects.get(email=request.user.email)
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'enrollment_capacity': request.data.get('enrollment_capacity'),
            'tutor': tutor.pk  # Set the tutor field to the ID of the active tutor
        }
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Tutor.DoesNotExist:
        return Response({'error': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
    
#view the courses of active tutor 
@api_view(['GET'])
def mycourses(request):
    try:
        Courses = Course.objects.filter(tutor=request.user.id)
    except Courses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(Courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_tutors(request):
    tutors = Tutor.objects.all()
    serializer = TutorSerializer(tutors, many=True)
    return Response(serializer.data)
""""
@api_view(['GET'])
def get_tutor_by_id(request, tutor_id):
    try:
        tutor = Tutor.objects.get(pk=tutor_id)
    except Tutor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TutorSerializer(tutor)
    return Response(serializer.data)
"""

    


#List all my students
@api_view(['GET'])
def tutor_students(request):
    try:
        # Get the courses of the active tutor
        tutor_courses = Tutor.objects.get(email=request.user.email).courses_tutored.all()
        
        # Get the students enrolled in those courses
        students = Student.objects.filter(courses_enrolled__in=tutor_courses)
        
        # Serialize the students
        serializer = StudentSerializer(students, many=True)
        
        return Response(serializer.data)
    except Tutor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#list my students by course     
@api_view(['GET'])
def tutor_students_by_course(request):
    try:
        # Get the active tutor
        tutor = Tutor.objects.get(email=request.user.email)

        # Get the courses taught by the tutor
        tutor_courses = tutor.courses_tutored.all()

        #dict to store course and corresponding students
        students_by_course = {}

        # Iterate through each course and retrieve students
        for course in tutor_courses:
            students = Student.objects.filter(courses_enrolled=course)
            serialized_students = StudentSerializer(students, many=True).data
            students_by_course[course.title] = serialized_students

        return Response(students_by_course)
    except Tutor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


 #return example : 
"""
 {
    'Math 101': [
        {'user_id': 1, 'username': 'student1', 'email': 'student1@example.com', 'role': 'STD', 'datejoined': '2023-01-01', 'firstname': 'John', 'lastname': 'Doe'},
        {'user_id': 2, 'username': 'student2', 'email': 'student2@example.com', 'role': 'STD', 'datejoined': '2023-02-01', 'firstname': 'Jane', 'lastname': 'Doe'}
    ],
    'Physics 202': [
        {'user_id': 3, 'username': 'student3', 'email': 'student3@example.com', 'role': 'STD', 'datejoined': '2023-03-01', 'firstname': 'Alice', 'lastname': 'Smith'},
        {'user_id': 4, 'username': 'student4', 'email': 'student4@example.com', 'role': 'STD', 'datejoined': '2023-04-01', 'firstname': 'Bob', 'lastname': 'Johnson'}
    ],
    # ... more courses and their corresponding students
}


"""

