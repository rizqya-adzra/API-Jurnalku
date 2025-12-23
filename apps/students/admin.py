from django.contrib import admin
from .models import Student, Jurusan, Rayon, Rombel


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nis',
        'user',
        'jurusan',
        'rayon',
        'rombel',
        'created_at',
    )

    list_select_related = ('user', 'jurusan', 'rayon', 'rombel')

    search_fields = (
        'name',
        'nis',
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'jurusan',
        'rayon',
        'rombel',
    )

    ordering = ('name',)


@admin.register(Jurusan)
class JurusanAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Rayon)
class RayonAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Rombel)
class RombelAdmin(admin.ModelAdmin):
    list_display = ('jurusan', 'tingkatan', 'nomor')
    list_filter = ('tingkatan',)
