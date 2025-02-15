from rest_framework import serializers

from apps.models import Attendance, Position, Branch, Shift, Employee


class PositionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name_uz', 'name_ru', 'name_en']


class BranchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name_uz', 'name_ru', 'name_en']


class ShiftModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'start_time', 'end_time', 'branches']


class AttendanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSearchFilterSerializer(serializers.Serializer):
    branch = serializers.IntegerField()
    date = serializers.DateField(required=False)
    search = serializers.CharField()


class KpiSerializer(serializers.Serializer):
    employee = serializers.IntegerField()
    price = serializers.IntegerField()
    status = serializers.CharField()
