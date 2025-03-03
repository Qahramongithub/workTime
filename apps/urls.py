from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views.attendance import AttendanceCreateAPIView, AttendanceListAPIView, AttendanceUpdateAPIView, \
    AttendanceFilterSearchAPIView
from apps.views.branch import BranchCreateApiView, BranchListApiView, BranchUpdateApiView, BranchDeleteApiView, \
    DayCreateApiView, DayListApiView, DayUpdateApiView, DayDeleteApiView, DayDetailApiView, BranchDetailApiView
from apps.views.group import GroupCreateApiView, GroupListApiView, GroupUpdateApiView, GroupDetailApiView, \
    GroupDeleteApiView, LessonStatusesView
# from apps.views.al import AlAPiView,  AlDataCreateAPiView
from apps.views.kpi import KpiApiView
from apps.views.position import PositionCreateApiView, PositionListApiView, PositionUpdateApiView, \
    PositionDetailApiView, PositionDeleteApiView
from apps.views.room import RoomCreateApiView, RoomListApiView, RoomUpdateApiView, RoomDetailApiView
from apps.views.student import StudentCreateApiView, StudentListApiView, StudentUpdateApiView, StudentDetailApiView, \
    StudentTeacherApiView, StudentDeleteApiView
from apps.views.teacher import EmployeeCreateApiView, EmployeeListApiView, EmployeeUpdateApiView, \
    EmployeeRetrieveApiView, \
    OneEmployeeListApiView, EmployeeDeleteApiView, TeacherEmployee

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# ============================================= Position ================================
urlpatterns += [
    path('position/create', PositionCreateApiView.as_view(), name='position_create'),
    path('position/list', PositionListApiView.as_view(), name='position_list'),
    path('position/update/<int:pk>', PositionUpdateApiView.as_view(), name='position_update'),
    path('position/delete/<int:pk>', PositionDeleteApiView.as_view(), name='position_delete'),
    path('position/detail/<int:pk>', PositionDetailApiView.as_view(), name='position_detail'),

]

# ============================================= Kpi ===========================================
urlpatterns += [
    path('kpi/create', KpiApiView.as_view(), name='kpi_create'),
]

# =============================================== Employee ====================================
urlpatterns += [
    path('employee/create', EmployeeCreateApiView.as_view(), name='employee_create'),
    path('employee/list', EmployeeListApiView.as_view(), name='employee_list'),
    path('employee/update/<int:pk>', EmployeeUpdateApiView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>', EmployeeDeleteApiView.as_view(), name='employee_delete'),
    path('employee/<int:pk>/', OneEmployeeListApiView.as_view(), name='employee'),
    path('employee/detail/<int:pk>', EmployeeRetrieveApiView.as_view(), name='employee_detail'),
    path('techear/list/<int:pk>', TeacherEmployee.as_view(), name='teacher'),
]

# =============================== Status ==============================================================
urlpatterns += [
    path('student/create', StudentCreateApiView.as_view(), name='student_create'),
    path('student/list', StudentListApiView.as_view(), name='student_list'),
    path('student/update/<int:pk>', StudentUpdateApiView.as_view(), name='student_update'),
    path('student/detail/<int:pk>', StudentDetailApiView.as_view(), name='student_detail'),
    path('student/techer/<int:pk>', StudentTeacherApiView.as_view(), name='student_teacher'),
    path('student/delete/<int:pk>', StudentDeleteApiView.as_view(), name='student_delete'),
]

# # ============================ Attendance =======================
urlpatterns += [
    path('attendance/create', AttendanceCreateAPIView.as_view(), name='attendance_create'),
    path('attendance/list', AttendanceListAPIView.as_view(), name='attendance_list'),
    path('attendance/update/<int:pk>', AttendanceUpdateAPIView.as_view(), name='attendance_update'),
    path('attendace/delete/<int:pk>', AttendanceUpdateAPIView.as_view(), name='attendance_update'),
    path('attendace/filter', AttendanceFilterSearchAPIView.as_view(), name='attendance_filter'),
]
# urlpatterns += [
#     path('al', AlAPiView.as_view(), name='al'),
#     path('al/create', AlDataCreateAPiView.as_view(), name='al_create'),
# ]
# ================================= Group ===============================================
urlpatterns += [
    path('group/create', GroupCreateApiView.as_view(), name='group_create'),
    path('group/list', GroupListApiView.as_view(), name='group_list'),
    path('group/update/<int:pk>', GroupUpdateApiView.as_view(), name='group_update'),
    path('group/detail/<int:pk>', GroupDetailApiView.as_view(), name='group_detail'),
    path('group/delete/<int:pk>', GroupDeleteApiView.as_view(), name='group_delete'),
    path('group/att/<int:pk>', LessonStatusesView.as_view(), name='group_att')
]

# ================================ Branch =================================================

urlpatterns += [
    path('branch/create', BranchCreateApiView.as_view(), name='branch_create'),
    path('branch/list', BranchListApiView.as_view(), name='branch_list'),
    path('branch/update/<int:pk>', BranchUpdateApiView.as_view(), name='branch_update'),
    path('branch/delete/<int:pk>', BranchDeleteApiView.as_view(), name='branch_delete'),
    path('branch/detail/<int:pk>', BranchDetailApiView.as_view(), name='branch_detail'),
]

# ======================================== Day ================================

urlpatterns += [
    path('day/create', DayCreateApiView.as_view(), name='day_create'),
    path('day/list', DayListApiView.as_view(), name='day_list'),
    path('day/update/<int:pk>', DayUpdateApiView.as_view(), name='day_update'),
    path('day/delete/<int:pk>', DayDeleteApiView.as_view(), name='day_delete'),
    path('day/detail/<int:pk>', DayDetailApiView.as_view(), name='day_detail')
]

# ======================================== Room ====================================
urlpatterns += [
    path('room/create', RoomCreateApiView.as_view(), name='room_create'),
    path('room/list', RoomListApiView.as_view(), name='room_list'),
    path('room/update/<int:pk>', RoomUpdateApiView.as_view(), name='room_update'),
    path('room/delete/<int:pk>', RoomDetailApiView.as_view(), name='room_delete')
]
