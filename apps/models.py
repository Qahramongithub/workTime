from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _


class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    branches = models.ManyToManyField('apps.Branch', related_name='shift')

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    class PriceType(models.TextChoices):
        HOUR = 'hour', _('Hour')
        DAY = 'day', _('Day')
        MONTH = 'month', _('Month')

    class SubPriceType(models.TextChoices):
        HOUR = 'hour', _('Hour')
        DAY = 'day', _('Day')
        MINUTE = 'min', _('Minute')

    status = models.CharField(max_length=100, choices=PriceType.choices, default=PriceType.MONTH)
    full_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')
    date = models.DateField(auto_now=False, default=date.today)
    shift = models.ForeignKey('apps.Shift', on_delete=models.CASCADE, related_name='employees')
    position = models.ForeignKey('apps.Position', on_delete=models.CASCADE, related_name='employees')
    dayoff = models.ManyToManyField('apps.Dayoff', related_name='employees', blank=True)
    subpricetype = models.CharField(max_length=100, choices=SubPriceType.choices, default=SubPriceType.HOUR)
    subprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name


class Attendance(models.Model):
    class Status(models.TextChoices):
        DELAY = 'delayed', _('Delayed')
        NOT_COME = 'not_come', _('Not Come')
        COME = 'come', _('Come')

    employee = models.ForeignKey('apps.Employee', on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now=False)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.NOT_COME)

    def __str__(self):
        return self.employee.full_name


class Kpi(models.Model):
    class KpiType(models.TextChoices):
        KPI = 'kpi', _('Kpi')
        AVANS = 'avans', _('Avans')

    kpi_type = models.CharField(max_length=100, choices=KpiType.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=False, default=date.today)
    employee = models.ForeignKey('apps.Employee', on_delete=models.CASCADE, related_name='kpi')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.employee.full_name


class Dayoff(models.Model):
    class DayoffType(models.TextChoices):
        MONDAY = 'monday', _('Monday')
        TUESDAY = 'tuesday', _('Tuesday')
        WEDNESDAY = 'wednesday', _('Wednesday')
        THURSDAY = 'thursday', _('Thursday')
        FRIDAY = 'friday', _('Friday')
        SATURDAY = 'saturday', _('Saturday')
        SUNDAY = 'sunday', _('Sunday')

    dayoff_type = models.CharField(max_length=100, choices=DayoffType.choices)

    def __str__(self):
        return self.get_dayoff_type_display()  # Dayoff'ning nomini olish
