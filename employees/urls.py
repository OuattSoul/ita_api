from rest_framework import routers
from .views import AppUserListView, AppUserProfileViewSet, CodeLoginUserView, EmployeeListViewSet,CongeViewSet,AssignMissionViewSet, ITAEmployeeView,RecruitmentRequestViewSet, RegisterUserView, TestViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register(r'employees-list', EmployeeListViewSet, basename='employees_list')
router.register(r'leaves/create', CongeViewSet, basename='conge')
router.register(r'missions/assign', AssignMissionViewSet, basename='assign_mission')
router.register(r'recruitment/requests', RecruitmentRequestViewSet, basename='recruitment_request')
router.register(r'user-profiles', AppUserProfileViewSet, basename='user-profile')
router.register(r'test-requests', TestViewSet, basename='test-request')
router.register(r'employees/list', ITAEmployeeView, basename='ita-employees') # GET


urlpatterns = router.urls + [
    path('employees-list/', EmployeeListViewSet.as_view({'get': 'list'}), name='employees-list'),
    path('staff/register/', RegisterUserView.as_view(), name='register-user'),
    path('users/list/', AppUserListView.as_view(), name='list-users'),
    path('staff/login/', CodeLoginUserView.as_view(), name='login-code'),
]
#urlpatterns = router.urls
