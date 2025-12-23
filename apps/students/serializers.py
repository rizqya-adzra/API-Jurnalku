from rest_framework import serializers
from .models import Student, Jurusan, Rayon, Rombel


class StudentSerializer(serializers.ModelSerializer):
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
        
class JurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurusan
        fields = '__all__'

class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'

class RombelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rombel
        fields = '__all__'
