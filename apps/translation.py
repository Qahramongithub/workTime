from modeltranslation.translator import register, TranslationOptions
from apps.models import Position, Employee, Student, Group, Day, Room, Branch


@register(Position)
class PositionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Branch)
class BranchTranslationOptions(TranslationOptions):
    fields = ('title', 'location',)


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('full_name',)


@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ('full_name',)


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('title',)

#
# @register(Day)
# class DayTranslationOptions(TranslationOptions):
#     fields = ('name',)


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('name',)
