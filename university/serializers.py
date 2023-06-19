from rest_framework import serializers

from university.models import Course, Address, Teacher, Student, Person


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Course
        fields=["name","credits","description"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["Country", "City", "Street", "Number"]


class PersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ["firstname","lastname","phonenumber","birthdate","address"]

class TeacherSerializer(serializers.ModelSerializer):

    course=CourseSerializer(many=True, read_only=True)
    person2=PersonSerializer(many=True, read_only=True)



    class Meta:
        model = Teacher
        fields = ["position", "course","person2"]



class StudentSerializer(serializers.ModelSerializer):
    person1 = PersonSerializer(many=True, read_only=True)
    class Meta:
        model=Student
        fields=["description","person1"]



