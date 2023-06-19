from django.contrib import admin
from .models import Course, Teacher, Student, Person, Address

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Person)
admin.site.register(Address)
