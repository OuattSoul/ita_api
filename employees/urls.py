from rest_framework import routers
from .views import EmployeeViewSet,CongeViewSet,AssignMissionViewSet,RecruitmentRequestViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'conges', CongeViewSet, basename='conge')
router.register(r'assign-missions', AssignMissionViewSet, basename='assign_mission')
router.register(r'recruitment-requests', RecruitmentRequestViewSet, basename='recruitment_request')


urlpatterns = router.urls
