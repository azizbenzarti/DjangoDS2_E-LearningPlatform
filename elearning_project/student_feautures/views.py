from rest_framework.decorators import api_view
from elearning_app.models import Tutor,Course,Student,Enrollment
from elearning_app.serializers import TutorSerializer,CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from admin_features.views import get_tutor_by_name



#view the courses of active Student 
@api_view(['GET'])
def enrolled_courses(request):
    try:
        student = Student.objects.get(email=request.user.email)
        enrolled_courses = student.courses_enrolled.all()
        if not enrolled_courses:
            return Response({'message': 'No courses yet'}, status=status.HTTP_200_OK)
        serializer = CourseSerializer(enrolled_courses, many=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

#view all tutors
@api_view(['GET'])
def list_tutors(request):
    tutors = Tutor.objects.all()
    serializer = TutorSerializer(tutors, many=True)
    return Response(serializer.data)

#view all courses 
@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

#view courses by title
@api_view(['GET'])
def view_courses_by_title(request, title):
    try:
        courses_with_title = Course.objects.filter(title__iexact=title)
        if not courses_with_title:
            return Response({'message': f'No courses found with the title "{title}"'}, status=status.HTTP_200_OK)
        serializer = CourseSerializer(courses_with_title, many=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)


#get course id
@api_view(['GET'])
def view_courses_by_tutor(request, tutor_name):
    try: 
        courses = Course.objects.filter(tutor__id=get_tutor_by_name['tutor_id']) #a tester ??
    except not courses:
        return Response({'message': f'No courses found by "{tutor_name}"'}, status=status.HTTP_200_OK)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def enroll_in_course(request, course_id):
    try:
        student = Student.objects.get(email=request.user.email)
        course = Course.objects.get(pk=course_id)

        if student.courses_enrolled.filter(pk=course_id).exists():
            return Response({'error': 'You are already enrolled in the course'}, status=status.HTTP_400_BAD_REQUEST)

        enrollment = Enrollment.objects.create(student=student, course=course)
        serializer = CourseSerializer(enrollment.course)

        return Response({'message': f'Student enrolled in course "{enrollment.course.title}" successfully', 'course': serializer.data})
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)