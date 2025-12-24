from rest_framework import serializers
from .models import Student, Jurusan, Rayon, Rombel
        
class JurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurusan
        fields = ['id', 'name']


class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = ['id', 'name']


class RombelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rombel
        fields = ['id', 'tingkatan']

class StudentSerializer(serializers.ModelSerializer):
    jurusan = JurusanSerializer(read_only=True)
    rayon = RayonSerializer(read_only=True)
    rombel = RombelSerializer(read_only=True)
    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'jurusan',
            'rayon',
            'rombel',
            'name',
            'nis',
            'photo',
            'created_at',
            'updated_at',
        ]