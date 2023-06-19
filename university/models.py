from django.db import models


class Teacher(models.Model):
    id=models.IntegerField(primary_key=True)
    position=models.CharField(max_length=45)

    def __str__(self):
        return self.position

class Course(models.Model):
    id=models.IntegerField(primary_key=True)
    course = models.ForeignKey(Teacher, related_name="course", on_delete=models.CASCADE)
    name=models.CharField(max_length=45)
    credits=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    description=models.TextField()

class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, related_name="person1", on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, related_name="person2", on_delete=models.CASCADE, null=True, blank=True)
    firstname=models.CharField(max_length=45)
    lastname=models.CharField(max_length=45)
    phonenumber=models.CharField(max_length=45)
    birthdate=models.DateTimeField()

class Address(models.Model):
    id=models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, related_name="address", on_delete=models.CASCADE)
    Country=models.CharField(max_length=45)
    City=models.CharField(max_length=45)
    Street=models.CharField(max_length=45)
    Number=models.IntegerField()
