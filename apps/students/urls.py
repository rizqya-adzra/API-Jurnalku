from django.urls import path
from .views import (
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
    JurusanListCreateView,
    JurusanRetrieveUpdateDestroyView,
    RayonListCreateView,
    RayonRetrieveUpdateDestroyView,
    RombelListCreateView,
    RombelRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        'students/',
        StudentListCreateView.as_view(),
        name='student-list-create'
    ),
    path(
        'students/<int:pk>/',
        StudentRetrieveUpdateDestroyView.as_view(),
        name='student-detail'
    ),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),

    path('majors/', JurusanListCreateView.as_view(), name='majors-list-create'),
    path('majors/<int:pk>/', JurusanRetrieveUpdateDestroyView.as_view(), name='majors-detail'),

    path('rayon/', RayonListCreateView.as_view(), name='rayon-list-create'),
    path('rayon/<int:pk>/', RayonRetrieveUpdateDestroyView.as_view(), name='rayon-detail'),

    path('rombel/', RombelListCreateView.as_view(), name='rombel-list-create'),
    path('rombel/<int:pk>/', RombelRetrieveUpdateDestroyView.as_view(), name='rombel-detail'),
]
