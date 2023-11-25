from rest_framework.routers import DefaultRouter
from .views import StudentViewSet,TutorViewSet,AdminViewSet,CourseViewSet,EnrollmentViewSet,MaterialViewSet,AssignmentViewSet,GradeViewSet,SubmissionViewSet,InteractionHistoryViewSet,ReadingStateViewSet

router = DefaultRouter()
router.register(r'tutors', TutorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'interaction-history', InteractionHistoryViewSet)
router.register(r'reading-states', ReadingStateViewSet)

urlpatterns = router.urls
