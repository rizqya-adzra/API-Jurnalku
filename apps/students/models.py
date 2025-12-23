from django.db import models
from apps.users.models import User
from django.core.validators import MinLengthValidator


class Jurusan(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rayon(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rombel(models.Model):
    jurusan = models.ForeignKey(
        Jurusan,
        on_delete=models.CASCADE,
        related_name='rombels'
    )
    tingkatan = models.PositiveSmallIntegerField()
    nomor = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('jurusan', 'tingkatan', 'nomor')
        ordering = ['jurusan', 'tingkatan', 'nomor']

    def __str__(self):
        return f"{self.jurusan.name} {self.tingkatan}-{self.nomor}"


class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='students'
    )
    jurusan = models.ForeignKey(
        Jurusan,
        on_delete=models.CASCADE,
        related_name='students'
    )
    rayon = models.ForeignKey(
        Rayon,
        on_delete=models.CASCADE,
        related_name='students'
    )
    rombel = models.ForeignKey(
        Rombel,
        on_delete=models.CASCADE,
        related_name='students'
    )

    name = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(7)]
    )
    nis = models.PositiveIntegerField(unique=True)
    photo = models.ImageField(
        upload_to='asset/student/photo/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        db_table = 'student_student'
        ordering = ['name']

    def __str__(self):
        return self.name
