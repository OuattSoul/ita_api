from rest_framework import routers
from .views import AppUserProfileViewSet, EmployeeListViewSet,CongeViewSet,AssignMissionViewSet,RecruitmentRequestViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register(r'employees-list', EmployeeListViewSet, basename='employees_list')
router.register(r'conges', CongeViewSet, basename='conge')
router.register(r'assign-missions', AssignMissionViewSet, basename='assign_mission')
router.register(r'recruitment-requests', RecruitmentRequestViewSet, basename='recruitment_request')
router.register(r'user-profiles', AppUserProfileViewSet, basename='user-profile')


urlpatterns = router.urls + [
    path('employees-list/', EmployeeListViewSet.as_view({'get': 'list'}), name='employees-list')
]
#urlpatterns = router.urls
