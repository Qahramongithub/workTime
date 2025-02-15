from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views.attendance import AttendanceCreateAPIView, AttendanceListAPIView, AttendanceUpdateAPIView, \
    AttendanceFilterSearchAPIView
from apps.views.branch import BranchCreateApiView, BranchListApiView, BranchUpdateApiView, ShiftCreateApiView, \
    ShiftListApiView, ShiftUpdateApiView
from apps.views.employee import EmployeeCreateApiView, EmployeeListApiView, EmployeeUpdateApiView, \
    OneEmployeeListApiView
from apps.views.kpi import KpiApiView
from apps.views.position import PositionCreateApiView, PositionListApiView, PositionUpdateApiView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# ============================================= Position ================================
urlpatterns += [
    path('position/create', PositionCreateApiView.as_view(), name='position_create'),
    path('position/list', PositionListApiView.as_view(), name='position_list'),
    path('position/update/<int:pk>', PositionUpdateApiView.as_view(), name='position_update'),
    path('position/delete/<int:pk>', PositionUpdateApiView.as_view(), name='position_delete'),

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
    path('employee/delete/<int:pk>', EmployeeUpdateApiView.as_view(), name='employee_delete'),
    path('employee/<int:pk>/', OneEmployeeListApiView.as_view(), name='employee'),
]

# ============================================= Branch =========================================
urlpatterns += [
    path('branch/create', BranchCreateApiView.as_view(), name='branch_create'),
    path('branch/list', BranchListApiView.as_view(), name='branch_list'),
    path('branch/update/<int:pk>', BranchUpdateApiView.as_view(), name='branch_update'),
    path('branch/delete/<int:pk>', BranchUpdateApiView.as_view(), name='branch_delete'),
]

# ============================================== Shift ==================================
urlpatterns += [
    path('shift/create', ShiftCreateApiView.as_view(), name='shift_create'),
    path('shift/list', ShiftListApiView.as_view(), name='shift_list'),
    path('shift/update/<int:pk>', ShiftUpdateApiView.as_view(), name='shift_update'),
    path('shift/delete/<int:pk>', ShiftUpdateApiView.as_view(), name='shift_delete'),
]

# ============================ Attendance =======================
urlpatterns += [
    path('attendance/create', AttendanceCreateAPIView.as_view(), name='attendance_create'),
    path('attendance/list', AttendanceListAPIView.as_view(), name='attendance_list'),
    path('attendance/update/<int:pk>', AttendanceUpdateAPIView.as_view(), name='attendance_update'),
    path('attendace/delete/<int:pk>', AttendanceUpdateAPIView.as_view(), name='attendance_update'),
    path('attendace/filter', AttendanceFilterSearchAPIView.as_view(), name='attendance_filter'),
]
