from rest_framework import serializers
from .models import School, Classroom, Teacher, ClassroomTeacher, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()  #

    class Meta:
        model = Classroom
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    
class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()  #

    class Meta:
        model = Student
        fields = '__all__'


class ClassroomTeacherSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = ClassroomTeacher
        fields = ['id', 'teacher', 'classroom']

class ClassroomTeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomTeacher
        fields = ['teacher', 'classroom']