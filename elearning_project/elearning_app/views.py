from rest_framework import viewsets

from .models import Admin, Tutor,Student,Course, Enrollment, Material, Assignment, Submission, Grade, InteractionHistory, ReadingState
from .serializers import StudentSerializer, TutorSerializer,AdminSerializer,CourseSerializer, EnrollmentSerializer, MaterialSerializer, AssignmentSerializer, SubmissionSerializer, GradeSerializer, InteractionHistorySerializer, ReadingStateSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer

class ReadingStateViewSet(viewsets.ModelViewSet):
    queryset = ReadingState.objects.all()
    serializer_class = ReadingStateSerializer
