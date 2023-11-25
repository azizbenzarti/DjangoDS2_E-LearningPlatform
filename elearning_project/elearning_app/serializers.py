from .models import Admin,Student,Tutor,Course,Enrollment,Material,Assignment,Submission,Grade,InteractionHistory,ReadingState
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer()
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Nested serializer for the student field
    course = CourseSerializer()  # Nested serializer for the course field
    class Meta:
        model = Enrollment
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    course = CourseSerializer() 
    class Meta:
        model = Material
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer() 
    class Meta:
        model = Assignment
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    assignment=AssignmentSerializer()
    class Meta:
        model = Submission
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    assignment=AssignmentSerializer()
    class Meta:
        model = Grade
        fields = '__all__'

class InteractionHistorySerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    material=MaterialSerializer()
    class Meta:
        model = InteractionHistory
        fields = '__all__'

class ReadingStateSerializer(serializers.ModelSerializer):
    student=StudentSerializer()
    material=MaterialSerializer()
    class Meta:
        model = ReadingState
        fields = '__all__'
