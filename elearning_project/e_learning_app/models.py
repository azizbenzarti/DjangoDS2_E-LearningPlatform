from django.db import models

class UserTypes(models.TextChoices):
    STUDENT='STD','Student'
    TUTOR='TUT','Tutor'
    ADMIN='ADM','Admin'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    role=models.CharField(max_length=4,choices=UserTypes.choices,default=UserTypes.STUDENT)
    datejoined = models.DateField()
    
    # ManyToMany tutor case
    courses_tutored = models.ManyToManyField('Course', related_name='tutors', blank=True)
    # ManyToMany student case
    courses_enrolled = models.ManyToManyField('Course', related_name='students', blank=True) 



    class Meta:
        db_table = "user"
        ordering=["role"]

    def __str__(self):
        return f'username={self.username},email={self.email},date joined={self.datejoined}'
    
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_capacity = models.IntegerField()

    class Meta:
        db_table = "course"
        ordering=["title"]
    def __str__(self):
        return f'title={self.title},tutor={self.tutor},enrollment_capacity={self.enrollment_capacity}'
    
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    upload_date = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=50)

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    due_date = models.DateTimeField()

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_content = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField()

class InteractionHistory(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interactions')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    interaction_date = models.DateTimeField(auto_now_add=True)

class ReadingState(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_states')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    read_state = models.FloatField()
    last_read_date = models.DateTimeField(auto_now=True)




