from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Teacher, Course, Student, Person, Address
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, AddressSerializer, PersonSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000

class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = LargeResultsSetPagination

class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LargeResultsSetPagination

class PersonViewset(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer