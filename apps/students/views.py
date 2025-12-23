from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from .models import Student, Jurusan, Rayon, Rombel
from .serializers import StudentSerializer, JurusanSerializer, RayonSerializer, RombelSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.select_related(
        'user',
        'jurusan',
        'rayon',
        'rombel',
    )
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_fields = [
        'jurusan',
        'rayon',
        'rombel',
    ]

    ordering_fields = [
        'name',
        'nis',
        'created_at',
    ]

    ordering = ['name']

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.select_related(
        'user',
        'jurusan',
        'rayon',
        'rombel',
    )
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class JurusanListCreateView(generics.ListCreateAPIView):
    queryset = Jurusan.objects.all()
    serializer_class = JurusanSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class JurusanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jurusan.objects.all()
    serializer_class = JurusanSerializer
    permission_classes = [AllowAny]

class RayonListCreateView(generics.ListCreateAPIView):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class RayonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer
    permission_classes = [AllowAny]

class RombelListCreateView(generics.ListCreateAPIView):
    queryset = Rombel.objects.select_related('jurusan')
    serializer_class = RombelSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['jurusan', 'tingkatan', 'nomor']
    ordering_fields = ['jurusan__name', 'tingkatan', 'nomor', 'created_at']
    ordering = ['jurusan__name', 'tingkatan', 'nomor']

class RombelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rombel.objects.select_related('jurusan')
    serializer_class = RombelSerializer
    permission_classes = [AllowAny]