import json
from random import choices

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ListField, IntegerField, DictField

from apps.models import Attendance, Position, Employee, Student, Group, Day, Branch, Room


class PositionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'title_uz', 'title_ru', 'title_en']


class BranchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'location_uz', 'location_ru', 'location_en']


class AttendanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class DayModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'name']


class EmployeeSerializer(serializers.Serializer):
    days = ListField(child=PrimaryKeyRelatedField(queryset=Day.objects.all()), required=False)
    full_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    seniority = serializers.IntegerField()
    age = serializers.IntegerField()
    photo = serializers.ImageField(required=False)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    password = serializers.CharField(max_length=255)
    positions = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=Employee.Gender, default=Employee.Gender.MALE)
    branch = serializers.IntegerField()

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name_uz', 'full_name_ru', 'full_name_en',
                  'phone_number', 'age', 'photo', 'balance', 'group_id', 'price']

    def validate(self, data):
        group = data.get('group_id')  # `group_id` emas, bevosita `group` olish
        if not group:
            raise serializers.ValidationError(_("Guruhni tanlang!"))

        # Guruhga necha o‘quvchi yozilganligini hisoblash
        student_count = group.students.count()  # Agar ManyToManyField bo‘lsa
        room = group.room  # Guruh xonasini olish

        if not room:
            raise serializers.ValidationError(_("Guruhga xona belgilanmagan!"))

        if student_count >= room.capacity:  # Xona hajmi bilan solishtirish
            raise serializers.ValidationError(
                _("Xona to‘lib bo‘lgan! Guruhni boshqa xonaga joylashtiring yoki boshqa guruhni tanlang.")
            )

        return data


class GroupModelSerializer(serializers.ModelSerializer):
    days = serializers.PrimaryKeyRelatedField(
        queryset=Day.objects.all(),
        many=True
    )

    def to_internal_value(self, data):
        """
        `days` malumotlarini to'g'ri formatga o'tkazish
        """
        data = data.copy()

        if "days" in data:
            if isinstance(data["days"], str):
                try:
                    data["days"] = [int(day.strip()) for day in data["days"].split(",")]
                except ValueError:
                    raise serializers.ValidationError({"days": _("Barcha qiymatlar integer bo‘lishi kerak!")})

        return super().to_internal_value(data)

    class Meta:
        model = Group
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'date', 'days',
                  'teacher', 'start_time', 'end_time', 'branch', 'room']

    def create(self, validated_data):
        days = validated_data.pop('days', [])  # `days` ni alohida olish
        group = Group.objects.create(**validated_data)  # Group yaratish
        group.days.set(days)  # ManyToManyField ga qiymatlar qo'shish
        return group

    def update(self, instance, validated_data):
        days = validated_data.pop('days', None)
        instance = super().update(instance, validated_data)
        if days is not None:
            instance.days.set(days)  # Eski kunlarni o'chirib, yangilarini qo'shish
        return instance

    # def validate(self, data):
    #     room = data.get('room')
    #     start_time = data.get('start_time')
    #     end_time = data.get('end_time')
    #     days = data.get('days')
    #     teacher = data.get('teacher')
    #
    #     # 📌 1️⃣ Xonani bandligi tekshiriladi
    #     if room and start_time and end_time and days:
    #         overlapping_groups = Group.objects.filter(
    #             room=room,
    #             days__in=days
    #         ).filter(
    #             start_time__lt=end_time,
    #             end_time__gt=start_time
    #         )
    #         if overlapping_groups.exists():
    #             raise serializers.ValidationError(_("❌ Xona ushbu vaqt oralig'ida band!"))
    #
    #     # 📌 2️⃣ O‘qituvchi bandligini tekshirish
    #     if teacher and start_time and end_time and days:
    #         overlapping_groups = Group.objects.filter(
    #             teacher=teacher,
    #             days__in=days
    #         ).filter(
    #             start_time__lt=end_time,
    #             end_time__gt=start_time
    #         )
    #         if overlapping_groups.exists():
    #             raise serializers.ValidationError(_("❌ O'qituvchi ushbu vaqt oralig'ida boshqa dars o'tmoqda!"))
    #
    #     # 📌 3️⃣ O‘qituvchining dam olish kuni ekanligini tekshirish
    #     if teacher and days:
    #         if isinstance(teacher, int):
    #             teacher = Employee.objects.get(id=teacher)
    #
    #         teacher_off_days = list(teacher.day.values_list("id", flat=True))
    #
    #         if any(day in teacher_off_days for day in days):
    #             raise serializers.ValidationError(_("❌ O'qituvchi ushbu kun dam olish kuni!"))
    #
    #     return data


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'count', 'branch']


class AttendanceSearchFilterSerializer(serializers.Serializer):
    branch = serializers.IntegerField()
    date = serializers.DateField(required=False)
    search = serializers.CharField()


class KpiSerializer(serializers.Serializer):
    employee = serializers.IntegerField()
    price = serializers.IntegerField()
    status = serializers.CharField()


class TestFileSerializer(serializers.ModelSerializer):
    pass

# class AlSerializer(serializers.Serializer):
#     string = serializers.CharField()
#
#
# class AlModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AlData
#         fields = '__all__'
