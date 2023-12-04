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
    
    class Meta:
        abstract=True
        ordering=["role"]

    def __str__(self):
        return f'username={self.username},email={self.email},date joined={self.datejoined}'
    
class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE) # tutor class passed as string beacuse it's not defined yet 
    enrollment_capacity = models.IntegerField()


    class Meta:
        db_table = "course"
        ordering=["title"]
    def __str__(self):
        return f'title={self.title},tutor={self.tutor},enrollment_capacity={self.enrollment_capacity}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.tutor.courses_tutored.add(self)
    
class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=4, choices=UserTypes.choices, default=UserTypes.STUDENT)

    class Meta:
        db_table="login"
        ordering=["email"]
        # email and password are unique together
        unique_together = ['email', 'password']
    
class Tutor(User):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    #relationship between Tutor and Courses (*-*)
    courses_tutored = models.ManyToManyField(Course, related_name='tutors', blank=True)
    #in this case we didn't specify where the many to many relationship data between Tutor and Courses is stored.
    # django will automatically create this table : elearning_app_tutor_courses behind the scenes. 
       
    class Meta:
        db_table='tutors'
        ordering=['lastname']

    def save(self, *args, **kwargs):
        # Automatically create a Login entry
        login = Login(email=self.email, role=UserTypes.TUTOR, password=self.password)
        login.save()
        super().save(*args, **kwargs)
    

    
class Student(User):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    #relationship between Student and Courses (*-*)
    courses_enrolled = models.ManyToManyField(Course, through='Enrollment', related_name='students', blank=True) 
    #through_fields is not necessary because Enrollment contains one FKey from Course and One FKey from Student 
    #related_name use : enrolled_students = course_instance.students.all()
    #the courses_enrolled field in the Student table is a representation of the many-to-many relationship, 
    # but it does not store the actual course data; that data is stored in the Enrollment table. 
    # The courses_enrolled field provides a convenient way to access and manage the enrolled courses for a specific student.
    # for example : enrolled_courses = student_instance.courses_enrolled.all()
    class Meta:
        db_table='student'
        ordering=['lastname']

    def save(self, *args, **kwargs):
        # Automatically create a Login entry
        login = Login(email=self.email, role=UserTypes.STUDENT, password=self.password)
        login.save()
        super().save(*args, **kwargs)
    



class Admin(User):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    class Meta:
        db_table='admin'
        ordering=['lastname']

    def save(self, *args, **kwargs):
        # Automatically create a Login entry
        login = Login(username=self.username,email=self.email, role=UserTypes.ADMIN, password=self.password)
        login.save()
        super().save(*args, **kwargs)

    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "enrollment"
        
class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    upload_date = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=50)
    class Meta:
        db_table = "material"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    due_date = models.DateTimeField()
    class Meta:
        db_table = "assignment"

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_content = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "submission"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField()
    class Meta:
        db_table = "grade"

class InteractionHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='interactions')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    interaction_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "interaction_history"



class ReadingState(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reading_states')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    read_state = models.IntegerField()  
    last_read_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "reading_state"



