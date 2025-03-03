# import gzip
# import io
# import zlib
#
# from PIL import Image
# from django.core.files.base import ContentFile
# from django.core.validators import FileExtensionValidator

from django.db import models
from django.db.models import CASCADE, IntegerField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# from pydub import AudioSegment


class Branch(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Kpi(models.Model):
    class Status(models.TextChoices):
        KPI = 'kpi', _('Kpi')
        AVANS = 'avans', _('Avans')

    status = models.CharField(choices=Status.choices, default=Status.KPI, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    teacher = models.ForeignKey('apps.Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    group_id = models.ForeignKey('apps.Group', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student/%Y/%m/%d', null=True, blank=True)
    age = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name


class Day(models.Model):
    class Days(models.TextChoices):
        MONDAY = 'monday', _('Monday / Dushanba / Понедельник')
        TUESDAY = 'tuesday', _('Tuesday / Seshanba / Вторник')
        WEDNESDAY = 'wednesday', _('Wednesday / Chorshanba / Среда')
        THURSDAY = 'thursday', _('Thursday / Payshanba / Четверг')
        FRIDAY = 'friday', _('Friday / Juma / Пятница')
        SATURDAY = 'saturday', _('Saturday / Shanba / Суббота')
        SUNDAY = 'sunday', _('Sunday / Yakshanba / Воскресенье')

    name = models.CharField(max_length=20, choices=Days.choices, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', _('Male')
        FEMALE = 'female', _('Female')

    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    seniority = models.IntegerField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='teacher/%Y/%m/%d', null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    branch = models.ManyToManyField('apps.Branch', blank=True, related_name='employees')
    days = models.ManyToManyField('apps.Day', blank=True, related_name='employees')
    gender = models.CharField(max_length=100, choices=Gender.choices, default=Gender.MALE)

    def __str__(self):
        return self.full_name


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    count = models.IntegerField(default=0)
    branch = models.ForeignKey('apps.Branch', CASCADE)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    class Status(models.TextChoices):
        COME = 'come', _('Come')
        NOT_COME = 'not_come', _('Not Come')
        NOT = 'not', _('Not')

    group = models.ForeignKey('apps.Group', on_delete=models.CASCADE)
    student = models.ForeignKey('apps.Student', on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, default=Status.NOT, max_length=100)
    date = models.DateField()
    statistics = models.FloatField()
    branch = models.ForeignKey('apps.Branch', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'student', 'date')

    def __str__(self):
        return self.student.full_name


class Group(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    days = models.JSONField(default=list)
    teacher = models.ForeignKey('apps.Employee', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    branch = models.ForeignKey('apps.Branch', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TestQuestion(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    file_name = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    text = models.TextField()
    options = models.JSONField()  # Variantlarni JSON sifatida saqlaymiz
    correct_answer = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        """Agar correct_answer bo‘sh bo‘lsa, birinchi variantni to‘g‘ri deb qabul qiladi"""
        if not self.correct_answer and self.options:
            self.correct_answer = self.options[0]  # Birinchi javob to‘g‘ri deb olinadi
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text

# class CompressedTextField(models.TextField):
#     """ Matnlarni avtomatik siqish va ochish """
#
#     def from_db_value(self, value, expression, connection):
#         if value is None:
#             return value
#         return zlib.decompress(value).decode("utf-8")
#
#     def get_prep_value(self, value):
#         if value is None:
#             return value
#         return zlib.compress(value.encode("utf-8"))

# class CompressedFileField(models.FileField):
#     """ Yuklangan fayllarni avtomatik siqish """
#
#     def save(self, name, content, save=True):
#         compressed_content = gzip.compress(content.read())
#         content = ContentFile(compressed_content)
#         content.name = name + ".gz"
#         super().save(name, content, save)

# class AlData(models.Model):
#     string = CompressedTextField(null=True, blank=True)  # 🔥 Matn siqib saqlanadi
#
#     images = models.ImageField(
#         upload_to='aldata/%Y/%m/%d',
#         validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif'])],
#         null=True, blank=True
#     )
#
#     audios = models.FileField(
#         upload_to='aldata/audios/%Y/%m/%d',
#         validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])],
#         null=True, blank=True
#     )
#
#     file = CompressedFileField(
#         upload_to='aldata/files/%Y/%m/%d',
#         validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'zip', 'mp4', 'txt', 'csv', 'xlsx'])],
#         null=True, blank=True
#     )
#
#     def __str__(self):
#         return self.string or "No Data"
#
#     def compress_image(self):
#         """ Rasmlarni avtomatik siqish """
#         if self.images:
#             image = Image.open(self.images.path)
#             image = image.convert("RGB")
#             output = io.BytesIO()
#             image.save(output, format="JPEG", quality=50)  # 50% sifat
#             self.images.save(self.images.name, ContentFile(output.getvalue()), save=False)
#
#     def compress_audio(self):
#         """ Audio fayllarni siqish (MP3, WAV, OGG) """
#         if self.audios:
#             audio = AudioSegment.from_file(self.audios.path)
#             compressed_audio_path = self.audios.path.replace(".wav", "_compressed.mp3")
#             audio.export(compressed_audio_path, format="mp3", bitrate="64k")  # 64 kbps sifat
#             self.audios.name = compressed_audio_path
#
#     def compress_all(self):
#         """ Hammasini siqish """
#         self.compress_image()
#         self.compress_audio()
#         self.save()
