from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.models import Employee, Kpi
from apps.serializer import KpiSerializer


@extend_schema(
    request=KpiSerializer,
    tags=['kpi'],
)
class KpiApiView(APIView):
    def post(self, request):
        employee_id = request.data.get('employee')
        price = request.data.get('price')
        status_value = request.data.get('status')

        employee = Employee.objects.filter(id=employee_id).first()

        if not employee:
            return Response({"error": "Xodim topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        if status_value == Kpi.Status.KPI:
            employee.balance += price
        elif status_value == Kpi.Status.AVANS:
            employee.balance -= price
        else:
            return Response({"error": "Noto‘g‘ri status."}, status=status.HTTP_400_BAD_REQUEST)

        # Balansni saqlash
        employee.save()

        # Yangilangan balansni qaytarish
        return Response({"employee_id": employee.id, "new_balance": employee.balance}, status=status.HTTP_200_OK)
