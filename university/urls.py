from django.urls import path
from rest_framework import routers
from .views import TeacherViewset, CourseViewset, StudentViewset, PersonViewset, AddressViewset

router=routers.DefaultRouter()
router.register(r"Teacher", TeacherViewset, basename="teachers")
router.register(r"Course", CourseViewset, basename="courses")
router.register(r"Student", StudentViewset, basename="students")
router.register(r"Person", PersonViewset, basename="persons")
router.register(r"Address", AddressViewset, basename="addresses")